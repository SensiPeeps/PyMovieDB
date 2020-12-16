import os
import pytest

from pymoviedb import Movie, TvShow
from pymoviedb.excs import TmdbApiError, ZeroResultsFound

api_key = os.getenv("TMDB_API")
movie, tvshow = Movie(api_key), TvShow(api_key)


class TestMovie:

    id = 299534
    imdb_id = "tt4154796"
    budget = 356000000
    homepage = "https://www.marvel.com/movies/avengers-endgame"
    release_date = "2019-04-24"
    poster_path = "/or06FN3Dka5tukK1e9sl16pB3iy.jpg"
    backdrop_path = "/7RyHsO4yDXtBv1zUU3mTpHeQ0d5.jpg"
    collection_id = 86311
    collection_name = "The Avengers Collection"
    collection_backdrop_path = "/zuW6fOiusv4X9nnW3paHGfXcSll.jpg"

    def test_search(self):
        res = movie.search("Avengers Endgame")["results"]
        assert res[0]["id"] == self.id
        assert res[0]["release_date"] == self.release_date
        assert res[0]["poster_path"] == self.poster_path

    def test_searchid(self):
        res = movie.searchid(299534)
        assert res["imdb_id"] == self.imdb_id
        assert res["budget"] == self.budget
        assert res["homepage"] == self.homepage
        assert res["backdrop_path"] == self.backdrop_path

    def test_search_collection(self):
        res = movie.search_collection("The Avengers")
        res = res["results"][0]
        assert res["backdrop_path"] == self.collection_backdrop_path
        assert res["id"] == self.collection_id

    def test_collection(self):
        res = movie.collection(86311)
        assert res["backdrop_path"] == self.collection_backdrop_path
        assert res["name"] == self.collection_name


class TestTvshow:

    id = 1396
    name = "Breaking Bad"
    first_air_date = "2008-01-20"
    last_air_date = "2013-09-29"
    homepage = "http://www.amc.com/shows/breaking-bad"
    episode_run_time = [45, 47]
    number_of_episodes = 62
    number_of_seasons = 5
    poster_path = "/ggFHVNu6YYI5L9pCfOacjizRGt.jpg"
    backdrop_path = "/tsRy63Mu5cu8etL1X7ZLyf7UP1M.jpg"

    def test_search(self):
        res = tvshow.search("Breaking bad")["results"]
        assert res[0]["id"] == self.id
        assert res[0]["name"] == self.name
        assert res[0]["first_air_date"] == self.first_air_date
        assert res[0]["poster_path"] == self.poster_path

    def test_searchid(self):
        res = tvshow.searchid(1396)
        assert res["homepage"] == self.homepage
        assert res["backdrop_path"] == self.backdrop_path
        assert res["last_air_date"] == self.last_air_date
        assert res["episode_run_time"] == self.episode_run_time
        assert res["number_of_episodes"] == self.number_of_episodes
        assert res["number_of_seasons"] == self.number_of_seasons


class TestErrors:
    def test_zeroresults_error(self):
        with pytest.raises(ZeroResultsFound):
            tvshow.search("xssxsxsx")
        with pytest.raises(ZeroResultsFound):
            movie.search("xssxsxsx")

    def test_tmdbapi_error(self):
        with pytest.raises(TmdbApiError):
            tvshow.searchid("xssxsxsx")
        with pytest.raises(TmdbApiError):
            movie.searchid("xssxsxsx")
