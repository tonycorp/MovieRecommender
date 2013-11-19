import webapp2
from main_page import FrontPage
from listings import Listings
from admin import Admin
from userzone import UserZone
from importmovies import ImportMovies
from movie import MoviePage
from addrating import AddRating

app = webapp2.WSGIApplication([
    ('/', FrontPage),
    ('/listings', Listings),
    ('/admin', Admin),
    ('/userzone', UserZone),
    ('/importmovies', ImportMovies),
    ('/movie', MoviePage),
    ('/addrating', AddRating)
], debug=True)