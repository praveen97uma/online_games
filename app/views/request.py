import jinja2
import os
import webapp2

import app_settings

#Jinja2 template loader that loads all the templates
jinja_loader =  jinja2.FileSystemLoader(app_settings.TEMPLATE_DIR)
jinja_environment = jinja2.Environment(loader=jinja_loader)



class BaseRequestHandler(webapp2.RequestHandler):
	"""Base class that all the other request handlers must subcass from.
	"""
	
	def render(self):
		template = self.getTemplate()
		context = self.getContext(template_args);		
		self.response.out.write(template.render(context))
	
	def getContext(self, **kwargs):
		"""Returns the context dictionary for the current view.
		"""
		pass

	def templatePath(self):
		"""Returns the template path relative to the template directory.
		
		Usage:
			return '/tictactoe/index.html'		
		"""	
		pass
		
	def getTemplate(self):
		"""Returns the template object for the current view.
		"""
		template_path = self.templatePath();
		template = jinja_environment.get_template(template_path)
		return template

