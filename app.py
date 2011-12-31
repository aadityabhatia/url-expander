from google.appengine.api import memcache, urlfetch
import json
import logging
import time
import urllib
import urlparse
import webapp2

cacheDurationServiceList = 604800
cacheDurationTempRedirect = 86400

def getExpandURLServiceList():
	longURLServiceListURL = "http://api.longurl.org/v2/services?format=json"
	serviceList = memcache.Client().get("serviceList")
	if not serviceList:
		serviceList = json.loads(urlfetch.fetch(longURLServiceListURL).content).keys()
		serviceList.append("s.eagull.net")
		serviceList.append("t.eagull.net")
		memcache.Client().set("serviceList", serviceList, time=cacheDurationServiceList)
	return serviceList

def expandURL(url):
	memcacheClient = memcache.Client()
	expandURLObject = memcacheClient.get(url)
	shortenerKnown = False

	if expandURLObject:
		return expandURLObject

	serviceList = getExpandURLServiceList()

	if urlparse.urlparse(url).hostname in serviceList:
		logging.info("ExpandURL hostname known: %s", url)
		shortenerKnown = True

	response = urlfetch.fetch(url, method=urlfetch.HEAD, follow_redirects=False, allow_truncated=True)
	logging.info("ExpandURL response code: %s", response.status_code)

	if response.status_code == 405:
		response = urlfetch.fetch(url, follow_redirects=False, allow_truncated=True)
		logging.info("ExpandURL response code: %s", response.status_code)

	code = response.status_code
	if code == 301 or (shortenerKnown and (code == 302 or code == 303 or code == 307)):
		longURL = response.headers['Location']
		logging.info("ExpandURL response Location: %s", response.headers['Location'])
	else:
		longURL = url

	if response.status_code == 301:
		cacheDuration = 0
	else:
		cacheDuration = cacheDurationTempRedirect

	expandURLObject = {'longURL': longURL, 'statusCode': response.status_code, 'shortenerKnown': shortenerKnown, 'fetched': int(time.time())}
	memcacheClient.set(url, expandURLObject, time=cacheDuration)
	return expandURLObject

class AppRequestHandler(webapp2.RequestHandler):
	def get(self, url=''):

		if not url.strip():
			self.redirect("https://github.com/dragonsblaze/url-expander#readme")
			return

		shortURL = urllib.unquote(url)
		expandURLObject = expandURL(shortURL)
		self.response.out.write(json.dumps(expandURLObject))

app = webapp2.WSGIApplication([('/(.*)', AppRequestHandler)], debug=False)
