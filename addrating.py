import os
import jinja2
import webapp2
import logging
import json
from google.appengine.ext import ndb
from google.appengine.api import users
from models import Rating, UserRecord

JINJA_ENVIRONMENT = jinja2.Environment(
        loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
        extensions=['jinja2.ext.autoescape'])

class AddRating(webapp2.RequestHandler):
        def post(self):
                user = users.get_current_user()
                movie = self.request.get('movietitle')
                rating = self.request.get('rating')
                ratingBefore = 0

                myresponse = {}

                query = Rating.query(Rating.movietitle == movie, Rating.username == user)
                currentRating = None

                for q in query:
                    currentRating = q

                if currentRating == None:
                    currentRating = Rating(username = user, movietitle = movie, movierating = int(rating))
                else:
                    ratingBefore = currentRating.movierating
                    currentRating.movierating = int(rating)

                query = UserRecord.query(UserRecord.username == user)
                userRecord = None

                for q in query:
                    userRecord = q

                if userRecord == None:
                    userRecord = UserRecord(username = user, totalratings = int(rating), numofratings = 1, averagerating = float(rating))
                else:
                    userRecord.totalratings = userRecord.totalratings - ratingBefore + int(rating)
                    if ratingBefore == 0:
                        userRecord.numofratings += 1

                    userRecord.averagerating = float(userRecord.totalratings) / float(userRecord.numofratings)

                logging.debug("Rating: " + rating)
                logging.debug("Username: " + str(user))
                logging.debug("Movie: " + movie)
                currentRating.put()
                logging.debug("Total Ratings: " + str(userRecord.totalratings))
                logging.debug("Number of Ratings: " + str(userRecord.numofratings))
                logging.debug("Average Rating: " + str(userRecord.averagerating))
                userRecord.put()

                self.response.out.write(json.dumps(myresponse))
                
