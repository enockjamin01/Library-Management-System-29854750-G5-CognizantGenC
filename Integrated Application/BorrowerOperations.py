from prettytable import PrettyTable

class BorrowerOperations():
    """
    A class for performing CRUD operations on a 'borrowers' database table.

    Methods:
    --------
    add_borrower(cursor, db, name, contact):
        Adds a new borrower to the database.

    update_borrower(cursor, db, attribute, value, id):
        Updates a borrower's attribute in the database.

    delete_borrower(cursor, db, id):
        Deletes a borrower from the database.
    """

    @staticmethod
    def add_borrower(cursor,db,name,contact):
        """
        Adds a new borrower to the 'borrowers' table in the database.

        Parameters:
        -----------
        cursor : object
            Database cursor for executing queries.
        db : object
            Database connection object.
        name : str
            Name of the borrower.
        contact : str
            Contact information of the borrower.

        Raises:
        -------
        Exception
            If there is an error while executing the SQL command.

        """

        try:
            cursor.execute("SELECT borrower_id FROM borrowers")
            ids=cursor.fetchall()
            id=0
            if len(ids) == 0:
                command=f"INSERT INTO borrowers(borrower_id,name,contact) VALUES ({id},'{name}','{contact}')"
                cursor.execute(command)
                db.commit()
            else:
                id=ids[-1][0]+1
                command=f"INSERT INTO borrowers(borrower_id,name,contact) VALUES ({id},'{name}','{contact}')"
                cursor.execute(command)
                db.commit()

            print("+-----------------------------------------------------+")
            print("Borrower Added")
            print("+-----------------------------------------------------+")
            cursor.execute(f"SELECT * FROM borrowers WHERE borrower_id = {id}")
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
    def update_borrower(cursor,db,attribute,value,id):
        """
        Updates a specific attribute of a borrower in the 'borrowers' table.

        Parameters:
        -----------
        cursor : object
            Database cursor for executing queries.
        db : object
            Database connection object.
        attribute : str
            Attribute of the borrower to update (e.g., 'name', 'contact').
        value : str
            New value for the attribute.
        id : int
            ID of the borrower to update.

        Raises:
        -------
        Exception
            If there is an error while executing the SQL command.

        """

        try:
            command=f"UPDATE borrowers SET {attribute} = '{value}' WHERE borrower_id = {id}"
            cursor.execute(command)
            db.commit()

            print("+-----------------------------------------------------+")
            print("Borrower Updated")
            print("+-----------------------------------------------------+")
            cursor.execute(f"SELECT * FROM borrowers WHERE borrower_id = {id}")
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
    def delete_borrower(cursor,db,id):
        """
        Deletes a borrower from the 'borrowers' table in the database.

        Parameters:
        -----------
        cursor : object
            Database cursor for executing queries.
        db : object
            Database connection object.
        id : int
            ID of the borrower to delete.

        Raises:
        -------
        Exception
            If there is an error while executing the SQL command.

        """

        try:
            command=f"DELETE FROM borrowers WHERE borrower_id = {id}"
            cursor.execute(command)
            db.commit()

            print("+-----------------------------------------------------+")
            print("Borrower Deleted")
            print("+-----------------------------------------------------+")

            cursor.execute(f"SELECT * FROM borrowers")
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


