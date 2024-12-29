import sqlite3

#connect to database
connection = sqlite3.connect('crisis.db')

#create cursor
c = conn.cursor()

#create a table
c.execute ("""CREATE TABLE accounts (
full_name text,
username text,
id text,
password text,
email text,
word_count integer,
directive_count integer
)""")



