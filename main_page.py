import os
import jinja2
import webapp2
from datetime import date
from google.appengine.api import users

JINJA_ENVIRONMENT = jinja2.Environment(
        loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
        extensions=['jinja2.ext.autoescape'])

class FrontPage(webapp2.RequestHandler):
        def get(self):
                user = users.get_current_user()

                if user:
                        template_values = {'user' : user}
                        header_values = {'logout' : users.create_logout_url('/')}

                        template = JINJA_ENVIRONMENT.get_template('header.html')
                        self.response.write(template.render(header_values))         
                        template = JINJA_ENVIRONMENT.get_template('index.html')
                        self.response.write(template.render(template_values))
                        template = JINJA_ENVIRONMENT.get_template('footer.html')
                        self.response.write(template.render())
                else:
                    self.redirect(users.create_login_url(self.request.uri))