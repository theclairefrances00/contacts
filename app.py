import database

MENU_PROMPT = """ \n --- Contacts App ---
Please choose one of these options:

1) Add a new contact
2) See all
3) Find by first name
4) Update
5) Exit

Your selection:""" 

UPDATE_PROMPT = """ - Update Info - 
What would you like to update?

1) First name
2) Last name
3) Phone number
4) Email
5) Back

Your selection:""" 

def menu():
    while(user_input := input(MENU_PROMPT))!="5":
        if user_input == "1":
            first_name = input("Enter first name: ")
            last_name = input("Enter last name: ")
            phone_number = int(input("Enter phone number: "))
            email = input("Enter email: ")

            database.add_contact(connection, first_name, last_name, phone_number, email)
        elif user_input == "2":
            contacts = database.get_all_contacts(connection)

            for contact in contacts:
                print(f"ID: {contact[0]}\nName: {contact[1]} {contact[2]}\nPhone Number: ({contact[3]})\nEmail: {contact[4]}\n")
                
        elif user_input == "3":
            contact = input("Enter first name to find: ")
            contacts = database.get_contacts_by_name(connection, contact)
            
            for contact in contacts:
                print(f"Name: {contact[1]} {contact[2]}\nPhone Number: ({contact[3]})   \nEmail: {contact[4]}\n")

        elif user_input == "4":
            update()
        else:
            print("Invalid input, please try again!")

def update():
    to_update = input("Enter ID of contact to update: ")

    while(user_input := input(UPDATE_PROMPT))!="5":
        if user_input == "1":
            new_first_name = input("Input new first name:")
            database.update_contact_firstname(connection, new_first_name, to_update)
        elif user_input == "2":
            new_last_name = input("Input new last name:")
            database.update_contact_lastname(connection, new_last_name, to_update)
        elif user_input == "3":
            new_phone_number = input("Input new phone number:")
            database.update_contact_phone_number(connection, new_phone_number, to_update)
        elif user_input == "4":
            new_email = input("Input new email:")
            database.update_contact_email(connection, new_email, to_update)
        else:
            print("Invalid input, please try again!")

connection = database.connect()
database.create_table(connection)
menu()
