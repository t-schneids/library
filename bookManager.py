# 12/17/2024
# Authors: Umer Ayub, Theodore Schneider
# Purpose: To provide an interface for users to successfully
#          get book recommendations based on previous reads

#import requests
import json

class BookManager:
    def __init__(self, db_file='books_db.json'):
        """
            initialize a json file to act as a database for the user
            USAGE: BookManager() -- initializes a new db
                   BookManager(db_file='custom_db_json')
        """
        self.db_file = db_file

        try:
            with open(self.db_file, 'r') as file:
                self.books_db = json.load(file)
        except:
            self.books_db = {}

# making an updateeee

# design/implementation plan

# create a class that can export these functionalities:
# function that provides recommendations -- it just asks for input
    # def get_recommendations(self, book_title):
# function that can add books that the user has read to the 'db'
    def add_book(self, book_title):
        if book_title not in self.books_db:
            self.books_db[book_title] = {'Review': None, 'Rating': None, 'Recommend': None}
            self.__save_db()
        else: 
            print(f"{book_title} is already in the Database")
        

# function that allows user to review books that they have already read
    # def review_book(self, book_title, review):
# function that allows interactive use of all of these functions
    # def interactive(self):

    def printDB(self):
        print(self.books_db)

# PRIVATE FUNCTIONS: 
    # def __init__(self, db_file='books_db.json'):
    def __save_db(self):
        """Saved database info to external file"""
        with open(self.db_file, 'w') as file:
            json.dump(self.books_db, file, indent= 4)




