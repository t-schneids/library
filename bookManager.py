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
    def review_book(self, book_title, review, rating):
        self.add_book(book_title)
        #if book_title not in self.books_db:
         #   self.books_db[book_title] = {'Review': None, 'Rating': None, 'Recommend': None}
        #    self.__save_db()
        print("Starting review")
        self.books_db[book_title]['Review'] = review
        rating = int(rating)
        self.books_db[book_title]['Rating'] = rating
        if rating >= 7:
            self.books_db[book_title]['Recommend'] = True
        else:
            self.books_db[book_title]['Recommend'] = False
        self.__save_db()



# function that allows interactive use of all of these functions
    def interactive(self):
        continueLoop = True
        while continueLoop:
            print('')
            self.options()
            choice = input('Please provide your choice: ')
            choice = choice.lower()
            
            if choice == 'o':
                self.options
            elif choice == 'a':
                book = input('Provide a book title: ')
                self.add_book(book)
            elif choice == 'r':
                book = input('Provide a book title: ')
                review = input('Provide a book review: ')
                rating = input('Rate the book: ')
                self.review_book(book, review, rating)
            elif choice == 'g':
                print('Not implemented yet')
                #self.get_recommendations
            elif choice == 'p':
                self.printDB()
            elif choice == 'q':
                continueLoop = False
            elif choice == 'c':
                clear = input('Type c again to confirm clearing or type anything else to return to options: ')
                if clear == 'c':
                    self.clear_db()
                print('Database cleared')
            else:
                print('Not Valid Input')
                




        


    def options(self):
        print('Options: ')
        print('Type o to see options')
        print('Type a to add a book to the dictionary')
        print('Type r to review a book')
        print('Type g to get recommendations based off a book')
        print('Type p for showing the database')
        print('Type c for clear your database')
        print('Type q to quit')


    def printDB(self):
        print(self.books_db)

    def clear_db(self):
        self.books_db = {}
        self.__save_db()

# PRIVATE FUNCTIONS: 
    def __save_db(self):
        """Saved database info to external file"""
        with open(self.db_file, 'w') as file:
            json.dump(self.books_db, file, indent= 4)





