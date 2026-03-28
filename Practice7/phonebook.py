from connect import connect
import csv

conn = connect()

cur = conn.cursor()

def create_table():
    cur.execute(""" 
    CREATE TABLE IF NOT EXISTS phonebook(
        id SERIAL PRIMARY KEY,
        username VARCHAR(100),
        phone VARCHAR(20)
    )
    """)
    conn.commit()
    print("Table ready")


def insert_from_csv():
    with open("contacts.csv", newline="", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        for row in reader:
            cur.execute(
                "INSERT INTO phonebook (username, phone) VALUES (%s, %s)",
                (row["username"], row["phone"])
            )
    conn.commit()
    print("CSV loaded")

def insert_from_console():
    name = input("Enter name: ")
    phone = input("Enter phone: ")

    cur.execute(
        "INSERT INTO phonebook (username, phone) VALUES (%s, %s)",
        (name, phone)
    )
    conn.commit()
    print("Added from console")

def show_all_contacts():
    cur.execute("SELECT * FROM phonebook")
    rows = cur.fetchall()

    print("\nAll contacts:")
    for row in rows:
        print(row)

def search_by_username():
    name = input("Enter username to search: ")

    cur.execute(
        "SELECT * FROM phonebook WHERE username = %s",
        (name,)
    )
    rows = cur.fetchall()

    print("\nSearch result: ")
    for row in rows:
        print(row)

def search_by_phone_prefix():
    prefix = input("Enter phone prefix: ")

    cur.execute(
        "SELECT * FROM phonebook WHERE phone LIKE %s",
        (prefix + "%",)
    )
    rows = cur.fetchall()

    print("\nSearch result:")
    for row in rows:
        print(row)

def update_contact():
    name = input("Enter username to update: ")
    new_phone = input("Enter new phone: ")

    cur.execute(
        "UPDATE phonebook SET phone = %s WHERE username = %s",
        (new_phone, name)
    )
    conn.commit()
    print("Updated")

def delete_by_username():
    name = input("Enter username to delete: ")

    cur.execute(
        "DELETE FROM phonebook WHERE username = %s",
        (name,)
    )
    conn.commit()
    print("Deleted by username")

def delete_by_phone():
    phone = input("Enter phone to delete: ")

    cur.execute(
        "DELETE FROM phonebook WHERE phone = %s",
        (phone,)
    )
    conn.commit()
    print("Deleted by phone")

def menu():
    create_table()

    while True:
        print("\n--- PHONEBOOK MENU ---")
        print("1. Insert from CSV")
        print("2. Insert from console")
        print("3. Show all contacts")
        print("4. Search by username")
        print("5. Search by phone prefix")
        print("6. Update contact")
        print("7. Deletete by username")
        print("8. Delete by phone")
        print("0. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            insert_from_csv()
        elif choice == "2":
            insert_from_console()
        elif choice == "3":
            show_all_contacts()
        elif choice == "4":
            search_by_username()
        elif choice == "5":
            search_by_phone_prefix()
        elif choice == "6":
            update_contact()
        elif choice == "7":
            delete_by_username()
        elif choice == "8":
            delete_by_phone()
        elif choice == "0":
            break
        else:
            print("Invalid choice")

menu()

cur.close()
conn.close()
print("Connection closed")