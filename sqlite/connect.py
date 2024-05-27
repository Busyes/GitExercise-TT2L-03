import sqlite3

#connect to a database
conn = sqlite3.connect('database.db')

#create table
cursor = conn.cursor()

# Create a table
cursor.execute('''CREATE TABLE IF NOT EXISTS Info (
                    email TEXT ,
                    name TEXT NOT NULL,
                    password 
                )''')

# Insert a row of data
cursor.execute("INSERT INTO Info (email, name, password) VALUES ('amiraraheema05@gmail.com', 'mira', 'amira123')")

# Commit the transaction
conn.commit()

# Query the database
cursor.execute("SELECT * FROM Info")
rows = cursor.fetchall()

for row in rows:
    print(row)

# Close the connection
conn.close()