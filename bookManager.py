# 12/17/2024
# Authors: Umer Ayub, Theodore Schneider
# Purpose: To provide an interface for users to successfully
#          get book recommendations based on previous reads

import requests
import json
from datetime import date

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

# create a class that can export these functionalities:
# function that provides recommendations -- it just asks for input
    def get_recommendations(self):
        """Gets recommendations based off a book
        :param book_title: the title of the book
        """
        book_title = ""
        choice = input('Do you want a recommendation based on your most recent book title read (type recent)? Or do you want to provide a book title now (type provide)? ')
        if choice.lower() == 'provide':
            book_title = input('Enter book title: ')
        else:
            for key in self.books_db:
                if self.books_db[key]['Most Recent'] == True:
                    book_title = key

        api_url = f"https://www.googleapis.com/books/v1/volumes?q={book_title}"
        response = requests.get(api_url)
        if response.status_code == 200:
            books = response.json().get('items', [])

            OGAuthors = []
            for book in books:
                volumeInfo = book.get("volumeInfo", {})
                title = volumeInfo.get("title", "unknown")
                authors = volumeInfo.get("authors", "unknown")

                if title == book_title:
                    OGAuthors = authors
                    print(f"OG: {OGAuthors}")
                    break

            print("We recommend: ")
            
            self.__get_Books(book_title, books, False, OGAuthors)

            print()
            response = input('Would you like to see the description for each book? (y/n)')
            if response.lower() == 'y':
                self.__get_Books(book_title, books, True, OGAuthors)
        else:
            print("Failed to fetch recommendations.")
        
    def __get_Books(self, book_title, books, printRecommendations, OGAuthors):
        """Purpose: to find book recommendations given a book title
        :param book_title: the title of the book to search
        :param books: a list of books that pop up given book title
        :printRecommendations: a boolean indicating whether the user wants recommendations for the books"""
        
        for book in books: 
                # check if the book is what was originally searched
                # if yes, save author name. Use the name to filter out books for recommendation
                volumeInfo = book.get("volumeInfo", {})
                title = volumeInfo.get("title", "unknown")
                authors = volumeInfo.get("authors", "unknown")  # authors is a list of authors for a singular book
                description = volumeInfo.get("description", "unknown")
                
                
                # Check to see if current book is written by the same authors that wrote the book we searched for
                
                if authors != OGAuthors:
                    if printRecommendations:
                        print(f"Title: {title} , Book Author(s): {authors} , Book Description: {description}")
                        print()
                    else:
                        print(f"Title: {title} , Book Author(s): {authors}")
                        print()


    def add_book(self, book_title):
        """Adds a book to the database
        :param book_title: the title of the book
        """
        today = date.today().strftime("%m/%d/%Y")
        for booktitle in self.books_db:
            self.books_db[booktitle]['Most Recent'] = False

        if book_title not in self.books_db:
            self.books_db[book_title] = {'Review': None, 'Rating': None, 'Recommend': None, 'Date Entered': today, 'Most Recent': True}
            self.__save_db()
        else: 
            print(f"{book_title} is already in the Database")
        


    def review_book(self, book_title, review, rating):
        """Allows the user to review a book
        :param book_title: the title of the book
        :param review: the review of the book
        :param rating: the rating of the book
        """
        self.add_book(book_title)
        print("Starting review")
        self.books_db[book_title]['Review'] = review
        rating = int(rating)
        self.books_db[book_title]['Rating'] = rating
        if rating >= 7:
            self.books_db[book_title]['Recommend'] = True
        else:
            self.books_db[book_title]['Recommend'] = False
        self.__save_db()


    def interactive(self):
        """Allows the user to interact with the database"""
        continueLoop = True
        while continueLoop:
            print('')
            self.__options()
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
                self.get_recommendations()
            elif choice == 'p':
                self.printDB()
            elif choice == 'q':
                continueLoop = False
            elif choice == 'c':
                clear = input('Type c again to confirm clearing or type anything else to return to options: ')
                if clear == 'c':
                    self.clearDB()
                print('Database cleared')
            else:
                print('Not Valid Input')   


    def __options(self):
        """Prints out the options for the user in the interactive mode"""
        print('Options: ')
        print('Type o to see options')
        print('Type a to add a book to the dictionary')
        print('Type r to review a book')
        print('Type g to get recommendations based off a book')
        print('Type p for showing the database')
        print('Type c for clear your database')
        print('Type q to quit')


    def printDB(self):
        """prints the database"""
        print(self.books_db)

    def clearDB(self):
        """Clears the database"""
        self.books_db = {}
        self.__save_db()

# PRIVATE FUNCTIONS: 
    def __save_db(self):
        """Saved database info to external file"""
        with open(self.db_file, 'w') as file:
            json.dump(self.books_db, file, indent= 4)





