# URL Expander
The opposite of URL Shortener -- it provides a JSON API for retrieving information about short URLs.

## Response Parameters
* `longURL`: URL resulting from first redirect
* `fetched`: UNIX timestamp representing the time when the information was fetched
* `shortenerKnown`: whether the short URL was creating using a known URL shortener
* `statusCode`: HTTP status code encountered when attempted to expand the URL

## Usage Examples
* http://url-expand.appspot.com/http%3A%2F%2Fis.gd%2Fw
* http://url-expand.appspot.com/http%3A//is.gd/w
* http://url-expand.appspot.com/http://is.gd/w

## Planned Features
* improved error handling
* option to fetch fresh results, skipping cache if it's older than "n" minutes
* option to recursively follow redirects
* fetch meta-data (e.g. title, description, canonical URL, shortlink) from destination

## Usage
The service endpoint `http://url-expand.appspot.com/` is subject to change without notice. It is recommended that you deploy this code to [AppEngine][1] using their [SDK][2] and use that as your service endpoint.

## Notes
* designed to run on [Google AppEngine](http://code.google.com/appengine/)
* inspired by [LongURL](http://longurl.org/)

[1]: http://appengine.google.com/ "AppEngine Dashboard"
[2]: http://code.google.com/appengine/downloads.html "AppEngine SDK Downloads"
