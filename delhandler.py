import tornado.web
from book import Book
import json


class DelHandler(tornado.web.RequestHandler):
    def initialize(self, books):
        self.books = books
        
    def get(self):
        title = self.get_argument('title')
        result = self.books.del_book(title)
        if result:
            self.write("Deleted book title: {0} successfully".format(title))
            self.set_status(200)
        else:
            self.write("Book '{0}' not found".format(title))
            self.set_status(404)
