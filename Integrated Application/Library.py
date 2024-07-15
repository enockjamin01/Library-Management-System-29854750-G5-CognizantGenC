import mysql.connector
from prettytable import PrettyTable
from BookOperations import BookOperations
from BorrowerOperations import BorrowerOperations
from BorrowingOperations import BorrowingOperations

class Library:

    """
    A class representing a Library Management System.

    Methods:
    --------
    display_table(cursor, table_name):
        Displays the contents of a specified table from the database.

    operations(cursor, db, option):
        Executes various operations based on the user's input option.

    """

    def display_table(self,cursor,table_name):

        """
        Displays the contents of a specified table from the database.

        Parameters:
        -----------
        cursor : object
            Database cursor for executing queries.
        table_name : str
            Name of the table to display.

        """


        print("+-----------------------------------------------------+")
        print(table_name," table")
        print("+-----------------------------------------------------+")
        cursor.execute(f"SELECT * FROM {table_name}")
        rows=cursor.fetchall()
        column_name=[des[0] for des in cursor.description]
        table=PrettyTable()
        table.field_names=column_name
        for row in rows:
            table.add_row(row)
        print(table)




    def operations(self,cursor,db,option):
        """
        Executes various operations based on the user's input option.

        Parameters:
        -----------
        cursor : object
            Database cursor for executing queries.
        db : object
            Database connection object.
        option : int
            User-selected option for operation.

        """

        match option:
            # Case 1: Display Table
            case 1:
                print("+-----------------------------------------------------+")
                print("0. Books")
                print("1. Borrowers")
                print("2. Borrowing")
                table_name=int(input("Select table to be displayed: "))
                tables=['books','borrowers','borrowing']
                if table_name > len(tables)-1:
                    print("Enter valid data")
                    print("+-----------------------------------------------------+")
                    return 0
                else:
                    self.display_table(cursor,tables[table_name])
                print("+-----------------------------------------------------+")

            # Case 2: Add Book
            case 2:
                try:
                    print("+-----------------------------------------------------+")
                    print("Adding Book: ")
                    print("+-----------------------------------------------------+")
                    title=input("Enter title of book: ")
                    author=input("Enter author of book: ")
                    genre=input("Enter genre of book: ")
                    price=float(input("Enter the price of book: "))
                    stock=int(input("Enter the number of stock: "))
                    BookOperations.add_book(cursor,db,title,author,genre,price,stock)
                except Exception:
                    print("+-----------------------------------------------------+")
                    print("Error while adding book")
                    print("+-----------------------------------------------------+")

            # Case 3: Update Book
            case 3:
                try:
                    print("+-----------------------------------------------------+")
                    print("Update Book: ")
                    print("+-----------------------------------------------------+")
                    self.display_table(cursor,"books")
                    print("+-----------------------------------------------------+")
                    print("1. Title")
                    print("2. Author")
                    print("3. Genre")
                    print("4. Price")
                    print("5. Stock")
                    print("+-----------------------------------------------------+")
                    attribute=int(input("Enter a attribute number: "))
                    attributes=["book_id","title","author","genre","price","stock"]
                    value=input("Enter the value: ")
                    id=int(input("Enter book id: "))
                    BookOperations.update_book(cursor,db,attributes[attribute-1],value,id)

                except Exception:
                    print("+-----------------------------------------------------+")
                    print("Error while updating book")
                    print("+-----------------------------------------------------+")

            # Case 4: Delete Book
            case 4:
                try:
                    print("+-----------------------------------------------------+")
                    print("Delete Book: ")
                    print("+-----------------------------------------------------+")
                    self.display_table(cursor,"books")
                    print("+-----------------------------------------------------+")
                    id=int(input("Enter book id: "))
                    print("+-----------------------------------------------------+")
                    BookOperations.delete_book(cursor,db,id)
                except Exception:
                    print("+-----------------------------------------------------+")
                    print("Error while deleting book")
                    print("+-----------------------------------------------------+")

            # Case 5: Add Borrower
            case 5:
                try:
                    print("+-----------------------------------------------------+")
                    print("Adding Borrower: ")
                    print("+-----------------------------------------------------+")
                    name=input("Enter name of borrower: ")
                    contact=input("Enter contact of borrower: ")
                    print("+-----------------------------------------------------+")
                    BorrowerOperations.add_borrower(cursor,db,name,contact)
                except Exception:
                    print("+-----------------------------------------------------+")
                    print("Error while deleting book")
                    print("+-----------------------------------------------------+")

            # Case 6: Update Borrower
            case 6:
                try:
                    print("+-----------------------------------------------------+")
                    print("Update Borrower: ")
                    print("+-----------------------------------------------------+")
                    self.display_table(cursor,"borrowers")
                    print("+-----------------------------------------------------+")
                    print("1. Name")
                    print("2. Contact")
                    print("+-----------------------------------------------------+")
                    attribute=int(input("Enter a attribute number: "))
                    attributes=["name","contact"]
                    value=input("Enter the value: ")
                    id=int(input("Enter borrowers id: "))
                    BorrowerOperations.update_borrower(cursor,db,attributes[attribute-1],value,id)

                except Exception:
                    print("+-----------------------------------------------------+")
                    print("Error while updating borrowers details")
                    print("+-----------------------------------------------------+")

            # Case 7: Delete Borrower
            case 7:
                try:
                    print("+-----------------------------------------------------+")
                    print("Delete Borrower Details: ")
                    print("+-----------------------------------------------------+")
                    self.display_table(cursor,"borrowers")
                    print("+-----------------------------------------------------+")
                    id=int(input("Enter borrower id: "))
                    print("+-----------------------------------------------------+")
                    BorrowerOperations.delete_borrower(cursor,db,id)
                except Exception:
                    print("+-----------------------------------------------------+")
                    print("Error while deleting borrower details")
                    print("+-----------------------------------------------------+")

            # Case 8: Borrow Book
            case 8:
                try:
                    print("+-----------------------------------------------------+")
                    print("Borrower Book: ")
                    print("+-----------------------------------------------------+")
                    print("Details: ")
                    print("1. New Borrower")
                    print("2. Existing Borrower")
                    print("+-----------------------------------------------------+")
                    user=int(input("Enter User status number: "))
                    print("+-----------------------------------------------------+")
                    if user == 1:
                        try:
                            print("+-----------------------------------------------------+")
                            print("Adding Borrower: ")
                            print("+-----------------------------------------------------+")
                            name=input("Enter name of borrower: ")
                            contact=input("Enter contact of borrower: ")
                            print("+-----------------------------------------------------+")
                            BorrowerOperations.add_borrower(cursor,db,name,contact)
                        except Exception:
                            print("+-----------------------------------------------------+")
                            print("Error while adding borrower")
                            print("+-----------------------------------------------------+")
                        try:
                            borrower_id=int(input("Enter borrower id: "))
                            print("+-----------------------------------------------------+")
                            self.display_table(cursor,"books")
                            print("+-----------------------------------------------------+")
                            book_id=int(input("Enter book id: "))
                            print("+-----------------------------------------------------+")
                            command=f"SELECT stock FROM books WHERE book_id = {book_id}"
                            cursor.execute(command)
                            stock=cursor.fetchall()[0][0]
                            quantity=int(input("Enter number of books to be borrowed: "))
                            if quantity > stock:
                                print("Stock not available")
                                command=f"SELECT * FROM books WHERE book_id = {book_id}"
                                cursor.execute(command)
                                rows=cursor.fetchall()
                                column_name=[des[0] for des in cursor.description]
                                table=PrettyTable()
                                table.field_names=column_name
                                for row in rows:
                                    table.add_row(row)
                                print(table)
                            else:
                                date=input("Enter date YYYY-MM-DD: ")
                                BorrowingOperations.add_book_borrow(cursor,db,book_id,borrower_id,quantity,date)
                        except:
                            print("+-----------------------------------------------------+")
                            print("Error while adding borrowed book")
                            print("+-----------------------------------------------------+")
                    elif user == 2:
                        try:
                            print("+-----------------------------------------------------+")
                            self.display_table(cursor,"borrowers")
                            print("+-----------------------------------------------------+")
                            borrower_id=int(input("Enter borrower id: "))
                            print("+-----------------------------------------------------+")
                            self.display_table(cursor,"books")
                            print("+-----------------------------------------------------+")
                            book_id=int(input("Enter book id: "))
                            print("+-----------------------------------------------------+")
                            command=f"SELECT stock FROM books WHERE book_id = {book_id}"
                            cursor.execute(command)
                            stock=cursor.fetchall()[0][0]
                            quantity=int(input("Enter number of books to be borrowed: "))
                            if quantity > stock:
                                print("Stock not available")
                                command=f"SELECT * FROM books WHERE book_id = {book_id}"
                                cursor.execute(command)
                                rows=cursor.fetchall()
                                column_name=[des[0] for des in cursor.description]
                                table=PrettyTable()
                                table.field_names=column_name
                                for row in rows:
                                    table.add_row(row)
                                print(table)
                            else:
                                date=input("Enter date YYYY-MM-DD: ")
                                BorrowingOperations.add_book_borrow(cursor,db,book_id,borrower_id,quantity,date)
                        except:
                            print("+-----------------------------------------------------+")
                            print("Error while adding borrowed book")
                            print("+-----------------------------------------------------+")
                    else:
                        print("+-----------------------------------------------------+")
                        print("Enter valid data")
                        print("+-----------------------------------------------------+")
                except Exception:
                    print("+-----------------------------------------------------+")
                    print("Error borrowing book")
                    print("+-----------------------------------------------------+")


            case 9:
                # Return book option
                try:
                    print("+-----------------------------------------------------+")
                    print("Return Book: ")
                    print("+-----------------------------------------------------+")
                    self.display_table(cursor,"borrowing")
                    print("+-----------------------------------------------------+")
                    borrowing_id=int(input("Enter borrowing id: "))
                    BorrowingOperations.return_book(cursor,db,borrowing_id)
                except:
                    print("+-----------------------------------------------------+")
                    print("Error returning book")
                    print("+-----------------------------------------------------+")

            case 10:
                # Exit option
                print("+-----------------------------------------------------+")
                print("Exiting Console")
                print("+-----------------------------------------------------+")
                cursor.close()
                db.close()
                quit()




# Establish database connection
db=mysql.connector.connect(
  host="localhost",
  user="root",
  password="TYPE YOUR ROOT PASSWORD HERE",
  database="library"
)

# Create cursor object
cursor = db.cursor()

# Flag to control program execution
flag=True

# Main program loop
while flag:
    print("+-----------------------------------------------------+")
    print("Library Management System")
    print("+-----------------------------------------------------+")
    print("1. Display Books")
    print("2. Add Books")
    print("3. Update Books")
    print("4. Delete Books")
    print("5. Add Borrower")
    print("6. Update Borrower")
    print("7. Delete Borrower")
    print("8. Borrow Book")
    print("9. Return Book")
    print("10. Exit")
    print("+-----------------------------------------------------+")
    options=int(input("Enter a number in the given options: "))
    print("+-----------------------------------------------------+")
    Library().operations(cursor,db,options)
    print("+-----------------------------------------------------+")