from prettytable import PrettyTable

class BorrowingOperations():
    """
    A class for handling borrowing and returning operations for books.

    Methods:
    --------
    add_book_borrow(cursor, db, book_id, borrower_id, quantity_borrowed, borrowing_date):
        Adds a record of book borrowing to the database and updates the stock.

    return_book(cursor, db, borrowing_id):
        Marks a book as returned in the borrowing records and updates the stock.
    """

    @staticmethod
    def add_book_borrow(cursor,db,book_id,borrower_id,quantity_borrowed,borrowing_date):
        """
        Adds a record of book borrowing to the 'borrowing' table in the database
        and updates the stock of the borrowed book.

        Parameters:
        -----------
        cursor : object
            Database cursor for executing queries.
        db : object
            Database connection object.
        book_id : int
            ID of the book being borrowed.
        borrower_id : int
            ID of the borrower.
        quantity_borrowed : int
            Number of copies of the book borrowed.
        borrowing_date : str
            Date of borrowing in 'YYYY-MM-DD' format.

        Raises:
        -------
        Exception
            If there is an error while executing the SQL command.

        """

        try:
            cursor.execute("SELECT borrowing_id FROM borrowing")
            ids=cursor.fetchall()
            id=0
            if len(ids) == 0:
                command=f"INSERT INTO borrowing(borrowing_id,book_id,borrower_id,quantity_borrowed,borrowing_date) VALUES ({id},{book_id},{borrower_id},{quantity_borrowed},'{borrowing_date}')"
                cursor.execute(command)
                db.commit()
                command=f"SELECT stock FROM books WHERE book_id = {book_id}"
                cursor.execute(command)
                stock=cursor.fetchall()[0][0]
                command=f"UPDATE books SET stock = {stock-quantity_borrowed} WHERE book_id = {book_id}"
                cursor.execute(command)
                db.commit()
            else:
                id=ids[-1][0]+1
                command=f"INSERT INTO borrowing(borrowing_id,book_id,borrower_id,quantity_borrowed,borrowing_date) VALUES ({id},{book_id},{borrower_id},{quantity_borrowed},'{borrowing_date}')"
                cursor.execute(command)
                db.commit()
                command=f"SELECT stock FROM books WHERE book_id = {book_id}"
                cursor.execute(command)
                stock=cursor.fetchall()[0][0]
                command=f"UPDATE books SET stock = {stock-quantity_borrowed} WHERE book_id = {book_id}"
                cursor.execute(command)
                db.commit()

            print("+-----------------------------------------------------+")
            print("Book Borrowed")
            print("+-----------------------------------------------------+")
            cursor.execute(f"SELECT * FROM borrowing WHERE borrowing_id = {id}")
            rows=cursor.fetchall()
            column_name=[des[0] for des in cursor.description]
            table=PrettyTable()
            table.field_names=column_name
            for row in rows:
                table.add_row(row)
            print(table)

            print("+-----------------------------------------------------+")
            print("Stock Left of Borrowed book")
            print("+-----------------------------------------------------+")
            cursor.execute(f"SELECT * FROM books WHERE book_id = {book_id}")
            rows=cursor.fetchall()
            column_name=[des[0] for des in cursor.description]
            table=PrettyTable()
            table.field_names=column_name
            for row in rows:
                table.add_row(row)
            print(table)

        except Exception:
            print("+-----------------------------------------------------+")
            print("Failed to borrow book")
            print("+-----------------------------------------------------+")

    @staticmethod
    def return_book(cursor,db,borrowing_id):

        """
        Marks a book as returned in the borrowing records and updates the stock of the returned book.

        Parameters:
        -----------
        cursor : object
            Database cursor for executing queries.
        db : object
            Database connection object.
        borrowing_id : int
            ID of the borrowing record to mark as returned.

        Raises:
        -------
        Exception
            If there is an error while executing the SQL command.

        """

        try:
            command=f"SELECT quantity_borrowed FROM borrowing WHERE borrowing_id = {borrowing_id}"
            cursor.execute(command)
            quantity_borrowed=cursor.fetchall()[0][0]

            command=f"SELECT book_id FROM borrowing WHERE borrowing_id = {borrowing_id}"
            cursor.execute(command)
            book_id=cursor.fetchall()[0][0]

            command=f"DELETE FROM borrowing WHERE borrowing_id = {borrowing_id}"
            cursor.execute(command)
            db.commit()

            command=f"SELECT stock FROM books WHERE book_id = {book_id}"
            cursor.execute(command)
            stock=cursor.fetchall()[0][0]

            command=f"UPDATE books SET stock = {stock+quantity_borrowed} WHERE book_id = {book_id}"
            cursor.execute(command)
            db.commit()

            print("+-----------------------------------------------------+")
            print("Book Returned")
            print("+-----------------------------------------------------+")

            print("Stock Left of Returned book")
            print("+-----------------------------------------------------+")
            cursor.execute(f"SELECT * FROM books WHERE book_id = {book_id}")
            rows=cursor.fetchall()
            column_name=[des[0] for des in cursor.description]
            table=PrettyTable()
            table.field_names=column_name
            for row in rows:
                table.add_row(row)
            print(table)

        except Exception:
            print("+-----------------------------------------------------+")
            print("Failed to return book")
            print("+-----------------------------------------------------+")


