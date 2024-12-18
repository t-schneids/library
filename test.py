from bookManager import BookManager as BM

def main():
    b = BM()
    b.add_book('Harry Potter 5')
    b.add_book('Harry Potter 2')
    b.add_book('Harry Potter 3')
    b.add_book('Harry Potter 4')
    b.printDB() 
    # b.clearDB()

main()