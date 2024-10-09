import os
from dotenv import load_dotenv  # For loading environment variables from .env file
import mysql.connector  # MySQL connector to interact with the database
from mysql.connector import Error  # Error handling for MySQL operations

load_dotenv()  # Load environment variables like DB credentials

# Function to establish a connection to the MySQL database
def create_connection():
    connection = None
    try:
        # Attempt to connect using environment variables for DB credentials
        connection = mysql.connector.connect(
            host=os.getenv('DB_HOST'),
            user=os.getenv('DB_USER'),
            password=os.getenv('DB_PASS'),
            database=os.getenv('hirehelper')
        )
        print("Successfully connected to the database")
    except Error as e:
        # Print detailed error information if connection fails
        print(f"Error connecting to MySQL: {e}")
    return connection

# Function to create the 'contacts' table if it doesn't already exist
def create_contacts(connection):
    create_table_query = """
    CREATE TABLE IF NOT EXISTS contacts (
        id INT AUTO_INCREMENT PRIMARY KEY,
        name VARCHAR(255) NOT NULL,
        grad INT,
        company VARCHAR(255),
        email VARCHAR(255),
        linkedin VARCHAR(255),
        title VARCHAR(255)
    )
    """
    try:
        # Execute the table creation query
        with connection.cursor() as cursor:
            cursor.execute(create_table_query)
            connection.commit()
            print("Table 'contacts' created successfully")
    except Error as e:
        print(f"Error creating table: {e}")

# Function to create the 'users' table if it doesn't already exist
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

# Function to add a new user to the 'users' table
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

# Function to add a new contact to the 'contacts' table
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

# Function to retrieve and display all users from the 'users' table
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
                    print(f"Major: {user[2]}")
                    print(f"Grad: {user[3]}")
                    print(f"Email: {user[4]}")
                    print(f"LinkedIn: {user[5]}")
    except Error as e:
        print(f"Error retrieving users: {e}")

# Function to retrieve and display all contacts from the 'contacts' table
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
                    print(f"Grad: {contact[2]}")
                    print(f"Company: {contact[3]}")
                    print(f"Email: {contact[4]}")
                    print(f"LinkedIn: {contact[5]}")
                    print(f"Title: {contact[6]}")
    except Error as e:
        print(f"Error retrieving contacts: {e}")

# Function to delete a user by their ID from the 'users' table
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

# Function to delete a contact by their ID from the 'contacts' table
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

# Main function to establish the database connection and create necessary tables
def main():
    connection = create_connection()  
    if connection is None:
        return  # Exit if connection fails
    
    create_contacts(connection)  # Ensure 'contacts' table exists
    create_users(connection)  # Ensure 'users' table exists
    
    connection.close()  

if __name__ == "__main__":
    main()  