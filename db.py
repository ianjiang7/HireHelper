import os
from dotenv import load_dotenv
import mysql.connector
from mysql.connector import Error

load_dotenv()

def create_connection():
    connection = None
    try:
        # Print connection details (be careful with this in production!)
        print(f"Attempting to connect to:")
        print(f"Host: {os.getenv('DB_HOST')}")
        print(f"User: {os.getenv('DB_USER')}")
        print(f"Database: {os.getenv('hirehelper')}")
        
        connection = mysql.connector.connect(
            host=os.getenv('DB_HOST'),
            user=os.getenv('DB_USER'),
            password=os.getenv('DB_PASS'),
            database=os.getenv('hirehelper')
        )
        print("Successfully connected to the database")
    except Error as e:
        print(f"Error connecting to MySQL: {e}")
        print(f"Error Code: {e.errno}")
        print(f"SQL State: {e.sqlstate}")
        print(f"Error Message: {e.msg}")
    return connection

# Create table if it doesn't exist
def create_contacts(connection):
    create_table_query = """
    CREATE TABLE IF NOT EXISTS contacts (
        id INT AUTO_INCREMENT PRIMARY KEY,
        name VARCHAR(255) NOT NULL,
        grad INT,
        company VARCHAR(255),
        email VARCHAR(255),
        linkedin VARCHAR(255)
        title VARCHAR(255)
    )
    """
    try:
        with connection.cursor() as cursor:
            cursor.execute(create_table_query)
            connection.commit()
            print("Table 'contacts' created successfully")
    except Error as e:
        print(f"Error creating table: {e}")
        
def create_users(connection):
    create_table_query = """
    CREATE TABLE IF NOT EXISTS users (
        id INT AUTO_INCREMENT PRIMARY KEY,
        name VARCHAR(255) NOT NULL,
        major VARCHAR(255),
        grad INT,
        email VARCHAR(255),
        linkedin VARCHAR(255)
        
    )
    """
    try:
        with connection.cursor() as cursor:
            cursor.execute(create_table_query)
            connection.commit()
            print("Table 'users' created successfully")
    except Error as e:
        print(f"Error creating table: {e}")
    
def add_user(connection, name, major, grade, email, linkedin):
    
    query = """
    INSERT INTO users (name, major, grade, email, linkedin)
    VALUES (%s, %s, %s, %s, %s)
    """
    values = (name, major, grade, email, linkedin)

    try:
        with connection.cursor() as cursor:
            cursor.execute(query, values)
            connection.commit()
            print(f"User added with ID: {cursor.lastrowid}")
    except Error as e:
        print(f"Error adding user: {e}")
    
def add_contact(connection, name, grad, company, email, linkedin, title):
    
    query = """
    INSERT INTO contacts (name, grad, company, email, linkedin, title)
    VALUES (%s, %s, %s, %s, %s, %s)
    """
    values = (name, grad, company, email, linkedin, title)

    try:
        with connection.cursor() as cursor:
            cursor.execute(query, values)
            connection.commit()
            print(f"Contact added with ID: {cursor.lastrowid}")
    except Error as e:
        print(f"Error adding contact: {e}")

def view_users(connection):
    query = "SELECT * FROM users"
    try:
        with connection.cursor() as cursor:
            cursor.execute(query)
            results = cursor.fetchall()
            if not results:
                print("No users found in the database.")
            else:
                for user in results:
                    print(f"\nID: {user[0]}")
                    print(f"Name: {user[1]}")
                    print(f"major: {user[2]}")
                    print(f"grad: {user[3]}")
                    print(f"email: {user[4]}")
                    print(f"linkedin: {user[5]}")

    except Error as e:
        print(f"Error retrieving users: {e}")

def view_contacts(connection):
    query = "SELECT * FROM contacts"
    try:
        with connection.cursor() as cursor:
            cursor.execute(query)
            results = cursor.fetchall()
            if not results:
                print("No contacts found in the database.")
            else:
                for contact in results:
                    print(f"\nID: {contact[0]}")
                    print(f"Name: {contact[1]}")
                    print(f"grad: {contact[2]}")
                    print(f"company: {contact[3]}")
                    print(f"email: {contact[4]}")
                    print(f"linkedin: {contact[5]}")
                    print(f"title: {contact[6]}")

    except Error as e:
        print(f"Error retrieving contacts: {e}")


def delete_user(connection, id):
    
    query = "DELETE FROM users WHERE id = %s"
    value = (id,)
    
    try:
        with connection.cursor() as cursor:
            cursor.execute(query, value)
            connection.commit()
            if cursor.rowcount:
                print("User deleted successfully!")
            else:
                print("No user found with that ID.")
    except Error as e:
        print(f"Error deleting user: {e}")

def delete_contacts(connection, id):
    
    query = "DELETE FROM contacts WHERE id = %s"
    value = (id,)
    
    try:
        with connection.cursor() as cursor:
            cursor.execute(query, value)
            connection.commit()
            if cursor.rowcount:
                print("Contact deleted successfully!")
            else:
                print("No contact found with that ID.")
    except Error as e:
        print(f"Error deleting contact: {e}")
        
    

def main():
    connection = create_connection()
    if connection is None:
        return
    
    create_contacts(connection)
    create_users(connection)

    
    

    connection.close()

if __name__ == "__main__":
    main()