# HireHelper
## Database Design
Using SQL, our data model consists of two tables, a users table and a contacts table. The users table is used to contain personal user data with columns including: id, name, major, graduation year, email, and linkedin. The contacts table is used to contain the information we will scrape from alumni. The columns include id, name, graduation year, current company, email, LinkedIn, and job position/title.

We chose SQL because we believed the data we store is very structured. The rigid columns that each data point will have like name and graduation year won't change so we will benefit the most by using SQL.

Intructions: To set up our database, run the create_connection() to establish a connection. Then run the create_contacts or create_users function to create the respective tables. To add rows into the table, use the respective add functions.
