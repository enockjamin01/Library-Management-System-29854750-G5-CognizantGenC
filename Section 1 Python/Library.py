from Activities import Activity
from LibraryManagments import LibraryManagment
from Books import Book

class Library:

    def operations(self,option,books,activity):
        """
        Perform various operations based on user input.

        Parameters:
        option (int): The user-selected option.
        books (list): List of Book objects representing the library inventory.
        activity (Activity): An instance of the Activity class to perform operations.

        Returns:
        None
        """
        a=activity
        match option:
            case 1:
                if len(books)>0:
                    a.display(books=books)
                else:
                    print("+-----------------------------------------------------+")
                    print("No books found")
                    print("+-----------------------------------------------------+")

            case 2:
                try:
                    print("+-----------------------------------------------------+")
                    print("Adding Book: ")
                    print("+-----------------------------------------------------+")
                    title=input("Enter title of book: ")
                    author=input("Enter author of book: ")
                    genre=input("Enter genre of book: ")
                    price=int(input("Enter the price of book: "))
                    stock=int(input("Enter the number of stock: "))
                    new_books=a.add_book(books,title,author,genre,price,stock)
                    books=new_books
                except Exception:
                    print("+-----------------------------------------------------+")
                    print("Error while adding book")
                    print("+-----------------------------------------------------+")

            case 3:
                try:
                    print("+-----------------------------------------------------+")
                    print("Update Book: ")
                    print("+-----------------------------------------------------+")
                    print("1. Title")
                    print("2. Author")
                    print("3. Genre")
                    print("4. Price")
                    print("5. Stock")
                    print("+-----------------------------------------------------+")
                    attribute=int(input("Enter a attribute number: "))
                    value=input("Enter the value: ")
                    id=int(input("Enter book id: "))
                    status=a.update_book(attribute=attribute,value=value,books=books,id=id)
                except Exception:
                    print("+-----------------------------------------------------+")
                    print("Error while updating")
                    print("+-----------------------------------------------------+")

            case 4:
                try:
                    print("+-----------------------------------------------------+")
                    print("Delete Book: ")
                    print("+-----------------------------------------------------+")
                    id=int(input("Enter book id: "))
                    books=LibraryManagment.delete(book_id=id,books=books)
                except Exception:
                    print("+-----------------------------------------------------+")
                    print("Error while deletion")
                    print("+-----------------------------------------------------+")

            case 5:
                try:
                    print("+-----------------------------------------------------+")
                    print("Book Availability: ")
                    print("+-----------------------------------------------------+")
                    id=int(input("Enter book id: "))
                    print("+-----------------------------------------------------+")
                    availability_status=a.availability(id,books)
                except Exception:
                    print("+-----------------------------------------------------+")
                    print("Error while checking availability")
                    print("+-----------------------------------------------------+")

            case 6:
                try:
                    print("+-----------------------------------------------------+")
                    print("Borrowing Book: ")
                    print("+-----------------------------------------------------+")
                    id=int(input("Enter book id: "))
                    borrow_number=int(input("Enter number of book to borrow: "))
                    borrow_status=a.borrow_book(book_id=id,books=books,borrow_number=borrow_number)
                except Exception:
                    print("+-----------------------------------------------------+")
                    print("Error while borrowing book")
                    print("+-----------------------------------------------------+")

            case 7:
                try:
                    print("+-----------------------------------------------------+")
                    print("Returing Book: ")
                    print("+-----------------------------------------------------+")
                    id=int(input("Enter book id: "))
                    return_number=int(input("Enter number of books returned: "))
                    return_status=a.return_book(book_id=id,books=books,return_number=return_number)
                except Exception:
                    print("+-----------------------------------------------------+")
                    print("Error while returning book")
                    print("+-----------------------------------------------------+")

            case 8:
                try:
                    print("+-----------------------------------------------------+")
                    print("Low Stock Books")
                    print("+-----------------------------------------------------+")
                    a.report_low_stock(books=books)
                except Exception:
                    print("+-----------------------------------------------------+")
                    print("Error while reporting book stocks")
                    print("+-----------------------------------------------------+")

            case 9:
                print("+-----------------------------------------------------+")
                print("Exiting Console")
                print("+-----------------------------------------------------+")
                flag=False
                quit()


# Initialize the library with dummy data
flag=True
dummy_data=[Book(0,"Pride and Prejudice","Jane Austen","character development",200,5),
            Book(1,"The Great Gatsby","F. Scott Fitzgerald","character development",900,10),
            Book(2,"To Kill a Mockingbird","Harper Lee","character development",1000,3)]
books=[]
books.extend(dummy_data)

# Main loop for the library management system
while flag:
    print("+-----------------------------------------------------+")
    print("Library Management System")
    print("+-----------------------------------------------------+")
    print("1. Display Books")
    print("2. Add Books")
    print("3. Update Books")
    print("4. Delete Books")
    print("5. Check Availability of Books")
    print("6. Borrow Books")
    print("7. Return Books")
    print("8. Report Low Stocks")
    print("9. Exit")
    print("+-----------------------------------------------------+")
    options=int(input("Enter a number in the given options: "))
    print("+-----------------------------------------------------+")
    library=Library().operations(books=books,option=options,activity=Activity())
    print("+-----------------------------------------------------+")