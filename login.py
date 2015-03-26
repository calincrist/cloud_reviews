__author__ = 'calincrist'

"""OpenID login page"""

from google.appengine.ext import webapp
from google.appengine.ext.webapp import template

from google.appengine.api import users
from google.appengine.ext import webapp
from google.appengine.ext.webapp.util import run_wsgi_app

providers = {
    'Google': 'https://www.google.com/accounts/o8/id'
}

class MainHandler(webapp.RequestHandler):
    def handle_openid(self, continue_url=None, openid_url=None):
        if openid_url:
            self.redirect(users.create_login_url(continue_url, None,
                                                 openid_url))
        else:
            self.response.out.write(template.render(
                'templates/login.html',
                {'google_url': users.create_login_url(federated_identity=providers.get('Google'))}))


    def get(self):
        continue_url = self.request.get('continue')
        openid_url = self.request.get('openid_identifier')
        self.handle_openid(continue_url, openid_url)

    def post(self):
        continue_url = self.request.get('continue')
        openid_url = self.request.get('openid_identifier')
        self.handle_openid(continue_url, openid_url)


application = webapp.WSGIApplication([
                                         ('.*', MainHandler),
                                     ], debug=True)


def main():
    run_wsgi_app(application)


if __name__ == '__main__':
    main()
