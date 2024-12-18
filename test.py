from bookManager import BookManager as BM

def main():
    b = BM()
    b.add_book('Harry Potter 1')
    b.add_book('Harry Potter 2')
    b.add_book('Harry Potter 3')
    b.printDB() 

main()