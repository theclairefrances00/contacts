import sqlite3

# All SQL
CREATE_CONTACTS_TABLE = """CREATE TABLE IF NOT EXISTS contacts (id INTEGER PRIMARY KEY,
        first_name TEXT, last_name TEXT, phone_number INTEGER, email TEXT);"""

INSERT_CONTACT = "INSERT INTO contacts (first_name, last_name, phone_number, email) VALUES(?,?,?,?);"

GET_ALL_CONTACTS = "SELECT * FROM contacts;"
GET_CONTACTS_BY_FIRSTNAME = "SELECT * FROM contacts WHERE first_name = ?;"
GET_CONTACTS_BY_ID = "SELECT * FROM contacts WHERE id = ?;"

UPDATE_FIRSTNAME = "UPDATE contacts SET first_name = ? WHERE id = ?;"
UPDATE_LASTNAME = "UPDATE contacts SET last_name = ? WHERE id = ?;"
UPDATE_PHONE_NUMBER = "UPDATE contacts SET phone_number = ? WHERE id = ?;"
UPDATE_EMAIL = "UPDATE contacts SET email = ? WHERE id = ?;"

DELETE_CONTACT_BY_FIRSTNAME = "DELETE FROM contacts WHERE first_name = ?;"


#create a connection to a db. If db doesnt exits this creates it
def connect():
    return sqlite3.connect('data.db')

def create_table(connection):
    with connection:
        connection.execute(CREATE_CONTACTS_TABLE)

def add_contact(connection, first_name, last_name, phone_number, email):
    with connection:
        connection.execute(INSERT_CONTACT, (first_name, last_name, phone_number, email))

# Get contacts
def get_all_contacts(connection):
    with connection:
        return connection.execute(GET_ALL_CONTACTS).fetchall()

def get_contacts_by_name(connection,first_name):
    with connection:
        return connection.execute(GET_CONTACTS_BY_FIRSTNAME, (first_name,)).fetchall()

def get_contact_by_id(connection,id):
    with connection:
        return connection.execute(GET_CONTACTS_BY_ID, (id,)).fetchall()

# Update functions
def update_contact_firstname(connection,first_name, id):
    with connection:
        connection.execute(UPDATE_FIRSTNAME, (first_name, id,))

def update_contact_lastname(connection,last_name, id):
    with connection:
        connection.execute(UPDATE_LASTNAME, (last_name, id,))

def update_contact_phone_number(connection,phone_number, id):
    with connection:
        connection.execute(UPDATE_PHONE_NUMBER, (phone_number, id,))

def update_contact_email(connection,email, id):
    with connection:
        connection.execute(UPDATE_EMAIL, (email, id,))

# Delete
def delete_contacts_by_name(connection,first_name):
    with connection:
        return connection.execute(DELETE_CONTACT_BY_FIRSTNAME, (first_name,)).fetchall()
