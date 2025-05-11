books = []

def listReader(title):
    for book in books:
        if book["title"].lower() == title.lower():
            return book
        return None 

def addBook(title, author, availableCopies, genre):
    books.append({
        "title":title, 
        "author":author,
        "availableCopies":availableCopies,
        "genre": genre
    })

def loanBook(title):
    book = listReader(title)
    if book != None:
        if book["availableCopies"] > 0:
            book["availableCopies"] -= 1
            print("You have successfully loaned the book.")
        else:
            print("No copies of this book are currently available.")

def returnBook(title):
    book = listReader(title)
    book["availableCopies"] += 1

def searchBook(title):
    book = listReader(title)
    if book:
        print(f"Title: {book["title"]}\nAuthor: {book["author"]}\nAvailable copies: {book["availableCopies"]}\nGenre: {book["genre"]}")

def deleteBook(title):
    book = listReader(title)
    books.remove(book)

def listGenre(genre):
    contador = 0
    for book in books:
        if book["genre"] == genre:
            contador += 1
            print(f"{contador}. {book["title"]}")

    if contador == 0:
        print("Currently there are no books from that genre.")

while True:
    try:
        option = int(input(f"¡Welcome to the library menu!\n1. Add books.\n2. Search books by title.\n3. Register book loan\n4. Return books.\n5. Delete books from the catalogue.\n6. List books by genre.\n7. Leave the menu.\nIntroduce your option: "))

        if option == 1:
            
            title = input("Introduce the title of the book: ")
            author = input("Introduce the author of the book: ")
            
            while True:
                try:
                    availableCopies = int(input("Introduce the amount of available copies (It must be above 0.): "))
                    if availableCopies <= 0:
                        print("The number must be above 0.")
                    else:
                        break
                except ValueError:
                    print("You must introduce a number, try again.")

            genre = input(f"Introduce the genre of the book (Fiction, Non-Fiction, Science, Biography, Children): ").strip().lower()

            while genre not in ("fiction", "non-fiction", "science", "biography", "children"):
                genre = input(f"Please introduce a valid genre.\nIntroduce the genre of the book (Fiction, Non-Fiction, Science, Biography, Children): ")
            
            addBook(title.capitalize(), author.capitalize(), availableCopies, genre.capitalize())
            print("¡Book added succesfully!")

        elif option == 2:
            title = input("Introduce the title of the book you want to search: ").strip()

            if listReader(title.capitalize()) != None:
                searchBook(title)
            else:
                print("That book doesn't exist, try again.")
        
        elif option == 3:
            title = input("Introduce the title of the book you want to loan: ").strip()

            if listReader(title.capitalize()) != None:
                loanBook(title)
            else:
                print("That book doesn't exist, try again.")
        
        elif option == 4:
            title = input("Introduce the title of the book you want to return: ").strip()

            if listReader(title.capitalize()) != None:
                returnBook(title)
                print("You have returned the loaned book.")
            else:
                print("That book doesn't exist, try again.")
        
        elif option == 5:
            title = input("Introduce the title of the book you want to delete from the catalogue: ")

            if listReader(title.capitalize()) != None:
                deleteBook(title)
                print("You have succesfully deleted the book.")
            else:
                print("That book doesn't exist, try again.")
        
        elif option == 6:

            genre = input("Introduce the genre: ").strip().lower()
            while genre not in ("fiction", "non-fiction", "science", "biography", "children"):
                genre = input(f"Please introduce a valid genre.\nIntroduce the genre of the book (Fiction, Non-Fiction, Science, Biography, Children): ").strip()
            listGenre(genre.capitalize)
        
        elif option == 7:
            print("You succesfully left the menu.")
            break

    except ValueError:
        print("You must introduce a number.")
