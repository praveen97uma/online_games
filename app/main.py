import webapp2


from modules.tictactoe.views.main_page import TicTacToeHandler

myapp = webapp2.WSGIApplication([
        ('/', TicTacToeHandler), 
        ],
        debug=True)
