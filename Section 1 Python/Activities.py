from LibraryManagments import LibraryManagment

class Activity():

    def display(self,books):
        """
        Display all books in the library in a tabular format.

        Parameters:
        books (list): A list of Book objects.

        Returns:
        None
        """
        print("Library Books")
        print("+-----------------------------------------------------+")
        headers=['Book ID','Title','Author','Genre','Price','Stock']
        header_row=" | ".join(headers)
        print(header_row)
        print("-"*len(header_row))
        for book in books:
            values=[book.get_id(),book.get_title(),book.get_author(),book.get_genre(),book.get_price(),book.get_stock()]
            row=" | ".join(str(value).ljust(20) for value in values)
            print(row)


    def availability(self,book_id,books):
        """
        Check availability of a book by its ID and print its details.

        Parameters:
        book_id (int): The ID of the book to check.
        books (list): A list of Book objects.

        Returns:
        int: 1 if book is found and printed, 0 otherwise.
        """
        for book in books:
            if book_id==book.get_id():
                if book.get_stock()>=5:
                    headers=['Book ID','Title','Price','Stock']
                    header_row=" | ".join(headers)
                    print(header_row)
                    print("-"*len(header_row))
                    values=[book.get_id(),book.get_title(),book.get_price(),book.get_stock()]
                    row=" | ".join(str(value).ljust(20) for value in values)
                    print(row)
                    return 1
                else:
                    headers=['Book ID','Title','Price','Stock']
                    header_row=" | ".join(headers)
                    print(header_row)
                    print("-"*len(header_row))
                    values=[book.get_id(),book.get_title(),book.get_price(),book.get_stock()]
                    row=" | ".join(str(value).ljust(20) for value in values)
                    print(row)
                    print("LOW STOCK OF BOOK")
                    return 1

        print("ID does not Exist")
        return 0

    def report_low_stock(self,books):
        """
        Display books with stock less than 5.

        Parameters:
        books (list): A list of Book objects.

        Returns:
        None
        """
        headers=['Book ID','Title','Author','Stock']
        header_row=" | ".join(headers)
        print(header_row)
        print("-"*len(header_row))
        for book in books:
            if book.get_stock()<5:
                values=[book.get_id(),book.get_title(),book.get_author(),book.get_stock()]
                row=" | ".join(str(value).ljust(20) for value in values)
                print(row)

    def borrow_book(self,book_id,books,borrow_number):
        """
        Borrow a specified number of copies of a book.

        Parameters:
        book_id (int): The ID of the book to borrow.
        books (list): A list of Book objects.
        borrow_number (int): Number of books to borrow.

        Returns:
        int: 1 if borrowing is successful, 0 otherwise.
        """
        print("+-----------------------------------------------------+")
        for book in books:
            if book.get_id()==book_id:
                if book.get_stock()<borrow_number:
                    headers=['Book ID','Title','Stock']
                    header_row=" | ".join(headers)
                    print(header_row)
                    print("-"*len(header_row))
                    values=[book.get_id(),book.get_title(),book.get_price(),book.get_stock()]
                    row=" | ".join(str(value).ljust(20) for value in values)
                    print(row)
                    print("Cannot borrow due to low stock")
                    return 1
                else:
                    headers=['Book ID','Title','Number of books borrowed']
                    header_row=" | ".join(headers)
                    print(header_row)
                    print("-"*len(header_row))
                    values=[book.get_id(),book.get_title()]
                    values.append(borrow_number)
                    row=" | ".join(str(value).ljust(20) for value in values)
                    print(row)
                    book.set_stock((book.get_stock()-borrow_number))
                    print("+-----------------------------------------------------+")
                    print("Stock Left After Borrow")
                    print("+-----------------------------------------------------+")
                    headers=['Book ID','Title','Stock']
                    header_row=" | ".join(headers)
                    print(header_row)
                    print("-"*len(header_row))
                    values=[book.get_id(),book.get_title(),book.get_price(),book.get_stock()]
                    row=" | ".join(str(value).ljust(20) for value in values)
                    print(row)
                    return 1

        print("ID does not Exist")
        return 0

    def return_book(self,book_id,books,return_number):
        """
        Return a specified number of copies of a borrowed book.

        Parameters:
        book_id (int): The ID of the book to return.
        books (list): A list of Book objects.
        return_number (int): Number of books to return.

        Returns:
        int: 1 if returning is successful, 0 otherwise.
        """
        print("+-----------------------------------------------------+")
        for book in books:
            if book.get_id()==book_id:
                headers=['Book ID','Title','Number of books returned']
                header_row=" | ".join(headers)
                print(header_row)
                print("-"*len(header_row))
                values=[book.get_id(),book.get_title()]
                values.append(return_number)
                row=" | ".join(str(value).ljust(20) for value in values)
                print(row)
                book.set_stock((return_number+book.get_stock()))
                print("+-----------------------------------------------------+")
                print("Stock Left After Return")
                print("+-----------------------------------------------------+")
                headers=['Book ID','Title','Stock']
                header_row=" | ".join(headers)
                print(header_row)
                print("-"*len(header_row))
                values=[book.get_id(),book.get_title(),book.get_price(),book.get_stock()]
                row=" | ".join(str(value).ljust(20) for value in values)
                print(row)
                return 1

        print("ID does not Exist")
        return 0

    def add_book(self,books,title,author,genre,price,stock):
        """
        Add a new book to the library.

        Parameters:
        books (list): A list of Book objects.
        title (str): The title of the new book.
        author (str): The author of the new book.
        genre (str): The genre of the new book.
        price (float): The price of the new book.
        stock (int): The stock quantity of the new book.

        Returns:
        list: Updated list of books after adding, or unchanged list if addition fails.
        """
        book=LibraryManagment.add(id=len(books),
                                      title=title,
                                      author=author,
                                      genre=genre,
                                      price=price,
                                      stock=stock)
        if book!=0:
            books.append(book)
            print("+-----------------------------------------------------+")
            print("Book added successfully")
            return books
        else:
            print("+-----------------------------------------------------+")
            print("Failed to add book")
            return books

    def update_book(self,attribute,value,id,books):
        """
        Update a specific attribute of a book.

        Parameters:
        attribute (int): The attribute to update (1=title, 2=author, 3=genre, 4=price, 5=stock).
        value (str/int): The new value for the attribute.
        id (int): The ID of the book to update.
        books (list): A list of Book objects.

        Returns:
        int: 1 if update is successful, 0 otherwise.
        """
        for book in books:
            if book.get_id()==id:
                update_status=LibraryManagment.update(book,attribute,value)
                if update_status != 0:
                    print("+-----------------------------------------------------+")
                    print("Updated Successfully")
                    print("+-----------------------------------------------------+")
                    headers=['Book ID','Title','Author','Genre','Price','Stock']
                    header_row=" | ".join(headers)
                    print(header_row)
                    print("-"*len(header_row))
                    values=[book.get_id(),book.get_title(),book.get_author(),book.get_genre(),book.get_price(),book.get_stock()]
                    row=" | ".join(str(value).ljust(20) for value in values)
                    print(row)
                    return 1

        print("ID does not Exist")
        return 0




