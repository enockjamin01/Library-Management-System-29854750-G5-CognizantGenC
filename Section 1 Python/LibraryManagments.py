from Books import Book

class LibraryManagment():

    @staticmethod
    def add(id,title,author,genre,price,stock):
        """
        Adds a new book to the library.

        Parameters:
        id (int): The ID of the book.
        title (str): The title of the book.
        author (str): The author of the book.
        genre (str): The genre of the book.
        price (float): The price of the book.
        stock (int): The stock quantity of the book.

        Returns:
        Book: A new Book object if creation is successful, otherwise 0.
        """
        try:
            book=Book(id=id,
                    title=title,
                    author=author,
                    genre=genre,
                    price=price,
                    stock=stock)
            return book
        except Exception:
            return 0

    @staticmethod
    def update(book,attribute,value):
        """
        Updates a specific attribute of a book.

        Parameters:
        book (Book): The book object to update.
        attribute (int): The attribute to update (1=title, 2=author, 3=genre, 4=price, 5=stock).
        value (str/int): The new value for the attribute.

        Returns:
        int: 1 if update is successful, otherwise 0.
        """
        if attribute == 1:
            book.set_title(value)
            return 1
        elif attribute == 2:
            book.set_author(value)
            return 1
        elif attribute == 3:
            book.set_genre(value)
            return 1
        elif attribute == 4:
            book.set_price(int(value))
            return 1
        elif attribute == 5:
            book.set_stock(book.get_stock()+int(value))
            return 1
        else:
            return 0

    @staticmethod
    def delete(books,book_id):
        """
        Deletes a book from the library by its ID.

        Parameters:
        books (list): A list of Book objects.
        book_id (int): The ID of the book to delete.

        Returns:
        list: Updated list of books after deletion, or unchanged list if deletion fails.
        """
        for i in range(0,len(books)):
            if book_id == books[i].get_id():
                books.pop(i)
                print("+-----------------------------------------------------+")
                print("Deletion Successful")
                return books
        print("+-----------------------------------------------------+")
        print("Deletion Failed")
        return books
