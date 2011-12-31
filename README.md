# URL Expander
This is the opposite of URL Shortener. It provides a JSON API for expanding short URLs, along with additional information about the expanded URL.

## Response parameters:
* `longURL`: URL resulting from first redirect
* `fetched`: UNIX timestamp representing the time when this URL was expanded
* `shortenerKnown`: whether the short URL is on the list of known URLs
* `statusCode`: HTTP status code encountered when attempted to expand the URL

## API examples:
* http://url-expand.appspot.com/http%3A%2F%2Fis.gd%2Fw
* http://url-expand.appspot.com/http%3A//is.gd/w
* http://url-expand.appspot.com/http://is.gd/w

## Planned features:
* improved error handling
* option to fetch fresh results, skipping cache if it's older than *n* minutes
* option to recursively follow redirects
* fetch meta-data (e.g. title, description, canonical URL, shortlink) from destination

It is designed to run on [Google AppEngine](http://code.google.com/appengine/). The project was inspired by [LongURL.org](http://longurl.org/).
