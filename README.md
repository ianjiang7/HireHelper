# HireHelper

#Data Model Description
### Users Table
- **person_id (PK)**: A unique identifier for each individual in the system.
- **education_id (FK)**: A foreign key linking to the user's education in the *Education* table.
- **name**: The full name of the user.
- **email**: The user's email address.
- **is_alumni**: A boolean indicating whether the individual is an alumni of an educational institution.
- **title**: The current job title or designation of the individual.

### Education Table
- **education_id (PK)**: A unique identifier for each education entry.
- **person_id (FK)**: A foreign key linking to the person who possesses this educational background.
- **school_name**: The name of the institution where the user obtained their education.
- **degree**: The type of degree earned (e.g., Bachelor's, Master's).
- **major**: The major or field of study.
- **start_date**: The date when the education program started.
- **end_date**: The date when the education program ended (or is expected to end).

### Connections Table
- **connection_id (PK)**: A unique identifier for each connection entry.
- **person_id (FK)**: A foreign key linking to the individual who is initiating the connection.
- **connection_user_id (FK)**: A foreign key linking to the user who is on the receiving end of the connection.
- **connection_status**: Represents the status of the connection (e.g., pending, accepted, declined).

### Experience Table
- **experience_id (PK)**: A unique identifier for each work experience entry.
- **person_id (FK)**: A foreign key linking to the individual who holds the work experience.
- **company_name**: The name of the company where the user gained this experience.
- **location**: The location of the company.
- **position**: The role or job title of the user at the company.
- **start_date**: The start date of the work experience.
- **end_date**: The end date of the work experience (if applicable).

### Relationships
- **Users to Education (One-to-Many)**: A user can have multiple education entries, but each education entry belongs to one user.
- **Users to Connections (Self-Referencing One-to-Many)**: A user can be connected to multiple other users, and each connection involves two users (one initiating and one receiving).
- **Users to Experience (One-to-Many)**: A user can have multiple work experiences, and each experience is linked to one user.

The model is designed to store user profiles, including their education history, work experience, and social connections within the platform. This structure allows for flexibility in tracking multiple education and experience entries per user and enables users to form connections with others on the platform.

# Why SQL
SQL is ideal for this project because it handles structured data with well-defined relationships between entities (like Users, Education, Experience, and Connections). It ensures data integrity through foreign keys, supports complex queries, and offers scalability and performance. Additionally, SQL databases come with a mature ecosystem, making them a strong choice for managing user profiles and connections.

# Instructions on how to set up database
Intructions: To set up our database, run the create_connection() to establish a connection. Then run the create_contacts or create_users function to create the respective tables. To add rows into the table, use the respective add functions.
