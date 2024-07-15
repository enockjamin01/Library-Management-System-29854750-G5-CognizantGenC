from prettytable import PrettyTable

class BookOperations():

    """
    A class for performing CRUD operations on a 'books' database table.

    Methods:
    --------
    add_book(cursor, db, title, author, genre, price, stock):
        Adds a new book to the database.

    update_book(cursor, db, attribute, value, id):
        Updates a book's attribute in the database.

    delete_book(cursor, db, id):
        Deletes a book from the database.
    """

    @staticmethod
    def add_book(cursor,db,title,author,genre,price,stock):
        """
        Adds a new book to the 'books' table in the database.

        Parameters:
        -----------
        cursor : object
            Database cursor for executing queries.
        db : object
            Database connection object.
        title : str
            Title of the book.
        author : str
            Author of the book.
        genre : str
            Genre of the book.
        price : float
            Price of the book.
        stock : int
            Number of copies in stock.

        Raises:
        -------
        Exception
            If there is an error while executing the SQL command.

        """

        try:
            cursor.execute("SELECT book_id FROM books")
            ids=cursor.fetchall()
            id=0
            if len(ids) == 0:
                command=f"INSERT INTO books(book_id,title,author,genre,price,stock) VALUES ({id},'{title}','{author}','{genre}',{price},{stock})"
                cursor.execute(command)
                db.commit()
            else:
                id=ids[-1][0]+1
                command=f"INSERT INTO books(book_id,title,author,genre,price,stock) VALUES ({id},'{title}','{author}','{genre}',{price},{stock})"
                cursor.execute(command)
                db.commit()

            print("+-----------------------------------------------------+")
            print("Book Added")
            print("+-----------------------------------------------------+")
            cursor.execute(f"SELECT * FROM books WHERE book_id = {id}")
            rows=cursor.fetchall()
            column_name=[des[0] for des in cursor.description]
            table=PrettyTable()
            table.field_names=column_name
            for row in rows:
                table.add_row(row)
            print(table)

        except Exception:
            print("+-----------------------------------------------------+")
            print("Failed to add data")
            print("+-----------------------------------------------------+")

    @staticmethod
    def update_book(cursor,db,attribute,value,id):
        """
        Updates a specific attribute of a book in the 'books' table.

        Parameters:
        -----------
        cursor : object
            Database cursor for executing queries.
        db : object
            Database connection object.
        attribute : str
            Attribute of the book to update (e.g., 'title', 'author', 'genre', 'price', 'stock').
        value : str or int or float
            New value for the attribute.
        id : int
            ID of the book to update.

        Raises:
        -------
        Exception
            If there is an error while executing the SQL command or if the value type is not compatible.

        """

        try:
            if isinstance(value,int) or isinstance(value,float):
                command=f"UPDATE books SET {attribute} = {value} WHERE book_id = {id}"
                cursor.execute(command)
                db.commit()

                print("+-----------------------------------------------------+")
                print("Book Updated")
                print("+-----------------------------------------------------+")
                cursor.execute(f"SELECT * FROM books WHERE book_id = {id}")
                rows=cursor.fetchall()
                column_name=[des[0] for des in cursor.description]
                table=PrettyTable()
                table.field_names=column_name
                for row in rows:
                    table.add_row(row)
                print(table)
            else:
                command=f"UPDATE books SET {attribute} = '{value}' WHERE book_id = {id}"
                cursor.execute(command)
                db.commit()

                print("+-----------------------------------------------------+")
                print("Book Updated")
                print("+-----------------------------------------------------+")
                cursor.execute(f"SELECT * FROM books WHERE book_id = {id}")
                rows=cursor.fetchall()
                column_name=[des[0] for des in cursor.description]
                table=PrettyTable()
                table.field_names=column_name
                for row in rows:
                    table.add_row(row)
                print(table)

        except Exception:
            print("+-----------------------------------------------------+")
            print("Failed to update data")
            print("+-----------------------------------------------------+")

    @staticmethod
    def delete_book(cursor,db,id):
        """
        Deletes a book from the 'books' table in the database.

        Parameters:
        -----------
        cursor : object
            Database cursor for executing queries.
        db : object
            Database connection object.
        id : int
            ID of the book to delete.

        Raises:
        -------
        Exception
            If there is an error while executing the SQL command.

        """

        try:
            command=f"DELETE FROM books WHERE book_id = {id}"
            cursor.execute(command)
            db.commit()

            print("+-----------------------------------------------------+")
            print("Book Deleted")
            print("+-----------------------------------------------------+")

            cursor.execute(f"SELECT * FROM books")
            rows=cursor.fetchall()
            column_name=[des[0] for des in cursor.description]
            table=PrettyTable()
            table.field_names=column_name
            for row in rows:
                table.add_row(row)
            print(table)

        except Exception:
            print("+-----------------------------------------------------+")
            print("Failed to delete data")
            print("+-----------------------------------------------------+")


