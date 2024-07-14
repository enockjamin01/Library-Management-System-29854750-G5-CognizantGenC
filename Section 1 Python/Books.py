class Book:

    def __init__(self,id,title,author,genre,price,stock):
        # Initialize a new Book object with provided attributes.
        self.id=id
        self.title=title
        self.author=author
        self.genre=genre
        self.price=price
        self.stock=stock

    def get_id(self):
        # Return the ID of the book.
        return self.id

    def get_title(self):
        # Return the title of the book.
        return self.title

    def get_author(self):
        # Return the author of the book.
        return self.author

    def get_genre(self):
        # Return the genre of the book.
        return self.genre

    def get_price(self):
        # Return the price of the book.
        return self.price

    def get_stock(self):
        # Return the stock quantity of the book.
        return self.stock

    def set_title(self,title):
        # Set a new title for the book.
        self.title=title

    def set_author(self,author):
        # Set a new author for the book.
        self.author=author

    def set_genre(self,genre):
        # Set a new genre for the book.
        self.genre=genre

    def set_price(self,price):
        # Set a new price for the book.
        self.price=price

    def  set_stock(self,stock):
        # Set a new stock quantity for the book.
        self.stock=stock