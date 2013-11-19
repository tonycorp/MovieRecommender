import os
import jinja2
import webapp2
import logging
import json
from google.appengine.ext import ndb
from google.appengine.api import users
from models import Rating

JINJA_ENVIRONMENT = jinja2.Environment(
        loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
        extensions=['jinja2.ext.autoescape'])

class AddRating(webapp2.RequestHandler):
        def post(self):
                user = users.get_current_user()
                movie = self.request.get('movietitle')
                rating = self.request.get('rating')

                myresponse = {}

                query = Rating.query(Rating.movietitle == movie, Rating.username == user)
                currentRating = None

                for q in query:
                    currentRating = q

                if currentRating == None:
                    currentRating = Rating(username = user, movietitle = movie, movierating = int(rating))
                else: 
                    currentRating.movierating = int(rating)

                logging.debug("Rating: " + rating)
                logging.debug("Username: " + str(user))
                logging.debug("Movie: " + movie)
                currentRating.put()

                self.response.out.write(json.dumps(myresponse))
                
