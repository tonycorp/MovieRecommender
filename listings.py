import os
import jinja2
import webapp2
import logging
from google.appengine.ext import ndb
from google.appengine.api import users
from models import Movie

JINJA_ENVIRONMENT = jinja2.Environment(
        loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
        extensions=['jinja2.ext.autoescape'])

class Listings(webapp2.RequestHandler):
        def get(self):
                user = users.get_current_user()
                movies = Movie.query()

                if user:
                        template_values = {'movies' : movies}
                        header_values = {'logout' : users.create_logout_url('/')}

                        for movie in movies:
                                logging.debug(movie.movietitle)

                        template = JINJA_ENVIRONMENT.get_template('header.html')
                        self.response.write(template.render(header_values))         
                        template = JINJA_ENVIRONMENT.get_template('listings.html')
                        self.response.write(template.render(template_values))
                        template = JINJA_ENVIRONMENT.get_template('footer.html')
                        self.response.write(template.render())
                else:
                    self.redirect(users.create_login_url(self.request.uri))
                