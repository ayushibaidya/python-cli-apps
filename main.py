def main():

    try:
        #initialize book list 
        booksList = []
        infile = open("theBooksList", "r")
        line = infile.readline()
        while line: 
            booksList.append(line.rstrip('\n').split(","))
            line = infile.readline()
        infile.close()
    except FileNotFoundError: 
        print("the <bookslist.txt> file is not found")
        print("Starting a new Books List")
        booksList = []

    choice = 0 

    while choice != 4: 
        print("Books Manager")
        print("1. Add a Book")
        print("2. Lookup a Book")
        print("3. Display Books")
        print("4. Quit")
        choice = int(input())

        if choice == 1: 
            print("Adding a book...")
            name_book = input("Enter the name of the Book: ")
            name_author = input("Enter the name of the Author: ")
            number_pages = input("Enter the number of Pages: ")  
            booksList.append([name_book, name_author, number_pages]) 
        elif choice == 2:
            print("Looking up for a Book...")  
            keyword = input("Enter Search Term: ")
            for book in booksList:
                if keyword in book: 
                    print(book)
        elif choice == 3:
            print("Displaying all books...")
            for i in range(len(booksList)):
                print(booksList[i])
        elif choice == 4:
            print("Quitting Program")
    print("Program has been terminated.")

    #saving to external TXT file 
    outfile = open("theBooksList.txt", "w")
    for book in booksList:
        outfile.write(",".join(book) + "\n")
    outfile.close()

if __name__ == "__main__":
    main()