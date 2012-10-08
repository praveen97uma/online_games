#!/usr/bin/env python

from base.views.request import BaseRequestHandler


class TicTacToeHandler(BaseRequestHandler):
	"""Class that handles the TicTacToe game.
	"""

	def templatePath(self):
		template_path = 'basetemplates/homepage.html'		
		return template_path

	def getContext(self):
		user = "Kamini Aditi"
		return {'user': user}

	def get(self):
		self.render()
