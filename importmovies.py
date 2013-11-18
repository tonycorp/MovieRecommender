import cgi
import webapp2
import lxml.html
import lxml.etree
import urllib
import datetime
from google.appengine.api import urlfetch
from google.appengine.ext import ndb
from models import Movie

class ImportMovies(webapp2.RequestHandler):
  def post(self):
    url = urlfetch.fetch('http://www.imdb.com/chart/top')
    doc = lxml.html.fromstring(url.content)

    movienumber = 1
    for row in doc.cssselect('tr'):
      if (row.get('class') == 'odd' or row.get('class') == 'even'):
        movie = Movie(id=movienumber)
        for column in row.cssselect('td'):
          if column.get('class') == 'posterColumn':
            for img in column.cssselect('img'):
              movie.movieimg = img.get('src')
          if column.get('class') == 'titleColumn':
            for title in column.cssselect('a'):
              movie.movietitle = title.text.encode('utf-8')
        movie.put()
        movienumber += 1

    self.redirect('/movielist')