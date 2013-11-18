from google.appengine.ext import ndb

class Movie(ndb.Model):
        movietitle = ndb.StringProperty()
        movieimg = ndb.StringProperty()

class Rating(ndb.Model):
        username = ndb.StringProperty()
        movietitle = ndb.StringProperty()
        movierating = ndb.IntegerProperty()