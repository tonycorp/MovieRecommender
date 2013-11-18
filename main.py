import webapp2
from main_page import FrontPage
from listings import Listings
from admin import Admin
from importmovies import ImportMovies

app = webapp2.WSGIApplication([
    ('/', FrontPage),
    ('/listings', Listings),
    ('/admin', Admin),
    ('/importmovies', ImportMovies)
], debug=True)