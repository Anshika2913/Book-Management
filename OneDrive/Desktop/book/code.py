import mysql.connector as sql
from mysql.connector import Error

# Establish a connection to the database
def get_db_connection():
    try:
        mydb = sql.connect(host='localhost', database='bookshop', user='root', password='admin', charset='utf8')
        return mydb
    except Error as e:
        print(f"Error connecting to MySQL: {e}")
        return None

# Create tables in the database
def create_tables():
    try:
        with get_db_connection() as mydb:
            if mydb.is_connected():
                c = mydb.cursor()
                c.execute("""
                    CREATE TABLE IF NOT EXISTS books (
                        b_id INT PRIMARY KEY,
                        book_name VARCHAR(255) NOT NULL,
                        author_name VARCHAR(255),
                        year VARCHAR(4),
                        price DECIMAL(10, 2),
                        type VARCHAR(50),
                        quantity INT
                    )
                """)
                c.execute("""
                    CREATE TABLE IF NOT EXISTS customers (
                        cno INT PRIMARY KEY,
                        cname VARCHAR(255) NOT NULL,
                        bookpurchase VARCHAR(255),
                        price DECIMAL(10, 2),
                        dateofpurchase DATE,
                        authorname VARCHAR(255),
                        contactno VARCHAR(15),
                        address TEXT
                    )
                """)
                mydb.commit()
                print("Tables created or verified.")
    except Exception as e:
        print(f"Error creating tables: {e}")

# Function for book details
def book():
    while True:
        print('*' * 95)
        print('\t\t\t\t\tBOOK DETAILS')
        print('*' * 95)
        print('''
        1 for adding book
        2 for displaying all book records
        3 for display one record
        4 for deleting all book records
        5 for deleting one record
        6 for modification in details of book
        7 to back to main menu
        ''')
        choice = int(input('Enter the key for following functions: '))
        if choice == 1:
            add()
        elif choice == 2:
            displayall()
        elif choice == 3:
            display()
        elif choice == 4:
            deleteall()
        elif choice == 5:
            delete()
        elif choice == 6:
            update()
        elif choice == 7:
            main()
        else:
            print('Invalid choice: Try again')

# Add book details
def add():
    try:
        ans = 'yes'
        while ans.lower() == 'yes':
            print('Enter book information....')
            b_id = input('Enter book ID: ')
            if not b_id.isdigit():
                print('Invalid book ID. Please enter a numeric value.')
                continue

            bname = input('Enter book name: ')
            if not bname:
                print('Book name cannot be empty.')
                continue

            aname = input('Enter author name: ')
            year = input('Enter year of publication: ')
            price = input('Enter price: ')
            if not price.replace('.', '', 1).isdigit():
                print('Invalid price. Please enter a numeric value.')
                continue

            itstype = input('Enter its type: ')
            quantity = input('Enter its quantity: ')
            if not quantity.isdigit():
                print('Invalid quantity. Please enter a numeric value.')
                continue

            query = """INSERT INTO books (b_id, book_name, author_name, year, price, type, quantity)
                       VALUES (%s, %s, %s, %s, %s, %s, %s)"""
            with get_db_connection() as mydb:
                if mydb.is_connected():
                    c = mydb.cursor()
                    c.execute(query, (int(b_id), bname, aname, year, float(price), itstype, int(quantity)))
                    mydb.commit()
                    print('Record added')
            ans = input('Enter yes to add more records: ')
    except mysql.connector.Error as e:
        print(f'Database error: {e}')
    except Exception as e:
        print(f'Something went wrong: {e}')

# Display all book details
def displayall():
    try:
        with get_db_connection() as mydb:
            if mydb.is_connected():
                c = mydb.cursor()
                c.execute('SELECT * FROM books')
                details = c.fetchall()
                for i in details:
                    print(i)
    except Exception as e:
        print('Something went wrong')
        print(e)

# Display selected book details
def display():
    try:
        bname = input('Enter name of book you want to display: ')
        with get_db_connection() as mydb:
            if mydb.is_connected():
                c = mydb.cursor()
                c.execute('SELECT * FROM books WHERE book_name = %s', (bname,))
                x = c.fetchone()
                print(x)
    except Exception as e:
        print('Something went wrong')
        print(e)

# Delete selected book
def delete():
    try:
        r = input('Enter book name whose record you want to delete: ')
        confirm = input(f'Are you sure you want to delete {r} (yes/no): ')
        if confirm.lower() == 'yes':
            with get_db_connection() as mydb:
                if mydb.is_connected():
                    c = mydb.cursor()
                    c.execute('DELETE FROM books WHERE book_name = %s', (r,))
                    mydb.commit()
                    print('Record deleted successfully')
    except Exception as e:
        print(f'Something went wrong: {e}')

# Delete all book records
def deleteall():
    try:
        r = input('Do you want to delete all records? (yes/no): ')
        if r.lower() == 'yes':
            with get_db_connection() as mydb:
                if mydb.is_connected():
                    c = mydb.cursor()
                    c.execute('DELETE FROM books')
                    mydb.commit()
                    print('All records deleted successfully')
    except Exception as e:
        print('Something went wrong')
        print(e)

# Update quantity/cost
def update():
    try:
        r = input('Enter book name whose details you want to update: ')
        n = int(input('Enter 1 to update quantity or 2 to update cost: '))
        with get_db_connection() as mydb:
            if mydb.is_connected():
                c = mydb.cursor()
                if n == 1:
                    m = int(input('Enter new quantity: '))
                    c.execute('UPDATE books SET quantity = %s WHERE book_name = %s', (m, r))
                elif n == 2:
                    b = float(input('Enter new cost: '))
                    c.execute('UPDATE books SET price = %s WHERE book_name = %s', (b, r))
                else:
                    print('Invalid choice: Try again')
                mydb.commit()
                print('Record updated successfully')
    except Exception as e:
        print('Something went wrong')
        print(e)

# Function for customer details
def cust():
    while True:
        print('*' * 95)
        print('\t\t\t\t\tCUSTOMER DETAILS')
        print('*' * 95)
        print('''
        1 for adding customer details
        2 for displaying all customer records
        3 for displaying one customer record
        4 for deleting all customer records
        5 for deleting one customer record
        6 for modification in customer details
        7 to back to main menu
        ''')
        choice = int(input('Enter the key for following functions: '))
        if choice == 1:
            custadd()
        elif choice == 2:
            custdisplayall()
        elif choice == 3:
            custdisplay()
        elif choice == 4:
            custdeleteall()
        elif choice == 5:
            custdelete()
        elif choice == 6:
            custupdate()
        elif choice == 7:
            main()
        else:
            print('Invalid choice: Try again')

# Add customer details
def custadd():
    try:
        ans = 'yes'
        while ans.lower() == 'yes':
            print('Enter customer information....')
            cid = int(input('Enter customer ID: '))
            cname = input('Enter name: ')
            book = input('Enter name of book purchased: ')
            price = float(input('Enter price: '))
            date = input('Enter date of purchase (YYYY-MM-DD): ')
            author = input('Enter author name: ')
            contact = input('Enter contact number: ')
            address = input('Enter address: ')
            query = """INSERT INTO customers (cno, cname, bookpurchase, price, dateofpurchase, authorname, contactno, address)
                       VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"""
            with get_db_connection() as mydb:
                if mydb.is_connected():
                    c = mydb.cursor()
                    c.execute(query, (cid, cname, book, price, date, author, contact, address))
                    mydb.commit()
                    print('Record added')
            ans = input('Enter yes to add more records: ')
    except Exception as e:
        print('Something went wrong')
        print(e)

# Display all customer details
def custdisplayall():
    try:
        with get_db_connection() as mydb:
            if mydb.is_connected():
                c = mydb.cursor()
                c.execute('SELECT * FROM customers')
                details = c.fetchall()
                for i in details:
                    print(i)
    except Exception as e:
        print('Something went wrong')
        print(e)

# Display selected customer details
def custdisplay():
    try:
        cid = int(input('Enter customer ID you want to display: '))
        with get_db_connection() as mydb:
            if mydb.is_connected():
                c = mydb.cursor()
                c.execute('SELECT * FROM customers WHERE cno = %s', (cid,))
                x = c.fetchone()
                print(x)
    except Exception as e:
        print('Something went wrong')
        print(e)

# Delete selected customer details
def custdelete():
    try:
        r = int(input('Enter customer ID whose record you want to delete: '))
        with get_db_connection() as mydb:
            if mydb.is_connected():
                c = mydb.cursor()
                c.execute('DELETE FROM customers WHERE cno = %s', (r,))
                mydb.commit()
                print('Record deleted successfully')
    except Exception as e:
        print('Something went wrong')
        print(e)

# Delete all customer records
def custdeleteall():
    try:
        r = input('Do you want to delete all customer records? (yes/no): ')
        if r.lower() == 'yes':
            with get_db_connection() as mydb:
                if mydb.is_connected():
                    c = mydb.cursor()
                    c.execute('DELETE FROM customers')
                    mydb.commit()
                    print('All customer records deleted successfully')
    except Exception as e:
        print('Something went wrong')
        print(e)

# Update customer details
def custupdate():
    try:
        r = int(input('Enter customer ID whose details you want to update: '))
        n = int(input('Enter 1 to update contact number or 2 to update address: '))
        with get_db_connection() as mydb:
            if mydb.is_connected():
                c = mydb.cursor()
                if n == 1:
                    m = input('Enter new contact number: ')
                    c.execute('UPDATE customers SET contactno = %s WHERE cno = %s', (m, r))
                elif n == 2:
                    b = input('Enter new address: ')
                    c.execute('UPDATE customers SET address = %s WHERE cno = %s', (b, r))
                else:
                    print('Invalid choice: Try again')
                mydb.commit()
                print('Record updated successfully')
    except Exception as e:
        print('Something went wrong')
        print(e)

# Main menu
def main():
    n = int(input('Enter 1 for book details\nEnter 2 for customer details: '))
    if n == 1:
        book()
    elif n == 2:
        cust()
    else:
        print('Invalid choice: Try again')

# Running the main function to start the application
create_tables()  # Ensure tables are created before starting
main()