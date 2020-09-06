# MIT License
#
# Copyright (c) 2020 Stɑrry Shivɑm
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.


from abc import ABC, abstractmethod
from requests import get
from .excs import TmdbApiError, ZeroResultsFound


class AbsMovieDB(ABC):
    """Abstract class for tmdb"""

    def __init__(self, api_key):
        """
        :param api_key :type str themoviedb API key.
        """
        self.api_key = api_key
        self.base_url = "https://api.themoviedb.org/3"

    @abstractmethod
    def search(self):
        pass


class Movie(AbsMovieDB):
    """This class handles all movie related tasks"""

    def search(self, query, language="en", page=1, inlude_adult="true"):
        """
        search for the query and return data in json format
        """

        payload = {
            "api_key": self.api_key,
            "language": language,
            "query": query,
            "page": page,
            "inlude_adult": inlude_adult,
        }

        resp = get(self.base_url + "/search/movie", params=payload)

        if resp.status_code == 200:

            check_res = resp.json()["results"]
            if len(check_res) <= 0:
                raise ZeroResultsFound(resp.text)
            return resp.json()
        else:
            raise TmdbApiError(resp.json())

    def searchid(self, movie_id, language="en", append_to_response="videos"):
        """
        returns movie detais for the movie_id in json format
        """

        payload = {
            "api_key": self.api_key,
            "language": language,
            "append_to_response": append_to_response,
        }

        resp = get(self.base_url + f"/movie/{movie_id}", params=payload)

        if resp.status_code == 200:
            return resp.json()
        raise TmdbApiError(resp.json())

    def recommendations(self, movie_id, language="en", page=1):
        """
        returns recommendations data for the movie_id in json format
        """

        payload = {"api_key": self.api_key, "language": language, "page": page}

        resp = get(self.base_url + f"/movie/{movie_id}/recommendations", params=payload)

        if resp.status_code == 200:
            return resp.json()
        raise TmdbApiError(resp.json())

    def trending(self, time_win="week"):
        """
        returns trending movies for time_win (day / week) in json format
        """
        payload = {"api_key": self.api_key}

        resp = get(self.base_url + f"/trending/movie/{time_win}", params=payload)

        if resp.status_code == 200:
            return resp.json()
        raise TmdbApiError(resp.json())


class TvShows(AbsMovieDB):
    """This class handles all tv related tasks"""

    def search(self, query, language="en", page=1, inlude_adult="true"):
        """
        search for the query and return data in json format
        """

        payload = {
            "api_key": self.api_key,
            "language": language,
            "query": query,
            "page": page,
            "inlude_adult": inlude_adult,
        }

        resp = get(self.base_url + "/search/tv", params=payload)

        if resp.status_code == 200:

            check_res = resp.json()["results"]
            if len(check_res) <= 0:
                raise ZeroResultsFound(resp.text)
            return resp.json()

        else:
            raise TmdbApiError(resp.json())

    def searchid(self, tv_id, language="en", append_to_response="videos"):
        """
        returns tv detais for the tv_id in json format
        """

        payload = {
            "api_key": self.api_key,
            "language": language,
            "append_to_response": append_to_response,
        }

        resp = get(self.base_url + f"/tv/{tv_id}", params=payload)

        if resp.status_code == 200:
            return resp.json()
        raise TmdbApiError(resp.json())

    def recommendations(self, tv_id, language="en", page=1):
        """
        returns recommendations data for the tv_id in json format
        """

        payload = {"api_key": self.api_key, "language": language, "page": page}

        resp = get(self.base_url + f"/movie/{tv_id}/recommendations", params=payload)

        if resp.status_code == 200:
            return resp.json()
        raise TmdbApiError(resp.json())

    def trending(self, time_win="week"):
        """
        returns trending tvshows for time_win (day / week) in json format
        """
        payload = {"api_key": self.api_key}

        resp = get(self.base_url + f"/trending/tv/{time_win}", params=payload)

        if resp.status_code == 200:
            return resp.json()
        raise TmdbApiError(resp.json())
