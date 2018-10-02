import webapp2
import urllib2
class DailyCronPage(webapp2.RequestHandler):
    def get(self):
        request = urllib2.Request('https://us-central1-clover-page-spee-1535578543408.cloudfunctions.net/google-speed-api-tester', headers={"cronrequest" : "true"})
        contents = urllib2.urlopen(request).read()

app = webapp2.WSGIApplication([
    ('/day', DailyrCronPage),
    ], debug=True)