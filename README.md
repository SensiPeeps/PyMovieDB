# PyMovieDB
<b>A simple python3 wrapper over themoviedb.org API</b>

[![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=flat-square)](http://makeapullrequest.com)
[![PyPI version](https://badge.fury.io/py/pymoviedb.svg)](https://badge.fury.io/py/pymoviedb)


## Install from PyPi
```pip install pymoviedb```

## Synopsis
```python
>>> from pymoviedb import Movie, TvShows
>>> APIKEY = "you-api-key"

# Create a Movie object
>>> mv = Movie(APIKEY)

# search for queries
>>> mv.search("Titanic")
# search using id
>>> mv.searchid(597)
# Get trending movies for "day" or "week"
# by default it's "week"
>>> mv.trending("day")
# Get recommendations by id
>>> mv.recommendations(597)

# Similarly for tvshows
>>> tv = TvShows(APIKEY)
>>> tv.search("Breaking bad")

# All methods can be found by using dir() function
print(dir(Movie))
```


## Handling exceptions
Exceptions can be imported from `pymoviedb.excs` for easy error handling.
Example:

```python
from pymoviedb.excs import ZeroResultsFound
tv = TvShows(APIKEY)

try:
    print(tv.search("xsxsxsx"))
except ZeroResultsFound:
     print("Nothing found!")
```  


## See also
TMDB API docs: https://developers.themoviedb.org/3/

This library is being used by my telegram bot bot [αcutєвσt](https://t.me/acutebot),
Check that out to see live working example!

Remember that this module not support all TMDB API methods yet.
## License

This module is licensed under the MIT license. See LICENSE file for more details.
