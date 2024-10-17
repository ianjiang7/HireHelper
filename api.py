from fastapi import FastAPI
import mysql  # MySQL connector to interact with the database
from mysql.connector import Error  # Error handling for MySQL operations
from db import *
app = FastAPI()

@app.get("/")
def home():
    return {}

@app.get("/person/")
def all_persons():
    #create connection
    connection = None
    json = {}
    try:
        # Attempt to connect using environment variables for DB credentials
        connection = mysql.connector.connect(
            host='34.44.42.132',
            user='hirehelper',
            password='hirehelper123!',
            database='hirehelper'
        )
        print("Successfully connected to the database")
    except Error as e:
        # Print detailed error information if connection fails
        print(f"Error connecting to MySQL: {e}")
    
    #select every entry in person
    query = "SELECT * FROM person"
    try:
        with connection.cursor() as cursor:
            cursor.execute(query)
            results = cursor.fetchall()
            if not results:
                print("No persons found in the database.")
            else:
                #create json containing each person
                for person in results:
                    json[person[0]] = {person[1],person[2],person[3],person[4]}
    except Error as e:
        print(f"Error retrieving users: {e}")
        
    return json

@app.get("/person/{person_id}")
def person(person_id):
    #create connection
    connection = None
    json = {}
    try:
        # Attempt to connect using environment variables for DB credentials
        connection = mysql.connector.connect(
            host='34.44.42.132',
            user='hirehelper',
            password='hirehelper123!',
            database='hirehelper'
        )
        print("Successfully connected to the database")
    except Error as e:
        # Print detailed error information if connection fails
        print(f"Error connecting to MySQL: {e}")
    
    # select person with matching ID
    query = f"SELECT * FROM person WHERE person_id = {person_id}"
    try:
        with connection.cursor() as cursor:
            cursor.execute(query)
            results = cursor.fetchall()
            if not results:
                print("No person found in the database.")
            else:
                # create json of person
                for person in results:
                    json[person[0]] = {person[1],person[2],person[3],person[4]}
    except Error as e:
        print(f"Error retrieving users: {e}")
        
    return json

@app.post("person/")
def create_person(name, title, industry, linkedin):
    #create connection
    connection = None
    json = {}
    try:
        # Attempt to connect using environment variables for DB credentials
        connection = mysql.connector.connect(
            host='34.44.42.132',
            user='hirehelper',
            password='hirehelper123!',
            database='hirehelper'
        )
        print("Successfully connected to the database")
    except Error as e:
        # Print detailed error information if connection fails
        print(f"Error connecting to MySQL: {e}")
    # use add_person method from db.py
    add_person(connection,name,title,industry,linkedin)
    
    # select and return the entry just added
    try:
        with connection.cursor() as cursor:
            cursor.execute(f"SELECT * FROM person WHERE name = {name} AND title = {title} AND industry = {industry} AND linkedin = {linkedin}")
            results = cursor.fetchall()
            if not results:
                print("No person found in the database.")
            else:
                for person in results:
                    json[person[0]] = {person[1],person[2],person[3],person[4]}
    except Error as e:
        print(f"Error retrieving users: {e}")
    return json
    
# @app.put("person/{person_id}")
# def update_person(person_id):
#     #create connection
#     connection = None
#     json = {}
#     try:
#         # Attempt to connect using environment variables for DB credentials
#         connection = mysql.connector.connect(
#             host='34.44.42.132',
#             user='hirehelper',
#             password='hirehelper123!',
#             database='hirehelper'
#         )
#         print("Successfully connected to the database")
#     except Error as e:
#         # Print detailed error information if connection fails
#         print(f"Error connecting to MySQL: {e}")
        
#     # Update the entry just added
#     try:
#         with connection.cursor() as cursor:
#             cursor.execute(f"UPDATE person SET name = {name}, title = {title}, industry = {industry}, linkedin = {linkedin} ")
#             results = cursor.fetchall()
#             if not results:
#                 print("No person found in the database.")
#             else:
#                 for person in results:
#                     json[person[0]] = {person[1],person[2],person[3],person[4]}
#     except Error as e:
#         print(f"Error retrieving users: {e}")
#     return json