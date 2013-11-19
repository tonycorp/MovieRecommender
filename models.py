from google.appengine.ext import ndb

class Movie(ndb.Model):
    movietitle = ndb.StringProperty()
    movieimg = ndb.StringProperty()

class Rating(ndb.Model):
    username = ndb.UserProperty()
    movietitle = ndb.StringProperty()
    movierating = ndb.IntegerProperty()

class Similarity(ndb.Model):
	userA = ndb.UserProperty()
	userB = ndb.UserProperty()
	similarity = ndb.FloatProperty()
