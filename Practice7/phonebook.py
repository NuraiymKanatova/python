from connect import connect
import csv
import re

conn = connect()
cur = conn.cursor()


def normalize_phone(phone):
    phone = phone.strip()
    # убираем пробелы, дефисы, скобки
    phone = re.sub(r"[^\d+]", "", phone)
    # формат 8701... -> +7701...
    if re.fullmatch(r"8\d{10}", phone):
        return "+7" + phone[1:]
    # формат +7701...
    if re.fullmatch("r\+7\d{10}", phone):
        return phone
    
    return None


def create_table():
    cur.execute(""" 
    CREATE TABLE IF NOT EXISTS phonebook(
        id SERIAL PRIMARY KEY,
        username VARCHAR(100) NOT NULL,
        phone VARCHAR(20) NOT NULL UNIQUE
    )
    """)
    conn.commit()
    print("Table ready")


def insert_from_csv():
    with open("contacts.csv", newline="", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        
        for row in reader:
            name = row["username"].strip()
            phone = normalize_phone(row["phone"])

            if phone is None:
                print(f"Invalid phone skipped: {row['phone']}")
                continue 

            cur.execute("""
                INSERT INTO phonebook (username, phone)
                VALUES (%s, %s)
                ON CONFLICT (phone)
                DO UPDATE SET username = EXCLUDED.username
            """, (name, phone))
    conn.commit()
    print("CSV loaded")


def insert_from_console():
    name = input("Enter name: ").strip()
    phone_input = input("Enter phone: (+7XXXXXXXXXX or 8XXXXXXXXXX): ").strip()

    phone = normalize_phone(phone_input)

    if phone is None:
        print("Invalid phone format. Use +7XXXXXXXXXX or 8XXXXXXXXXX")
        return

    cur.execute("""
        INSERT INTO phonebook (username, phone) 
        VALUES (%s, %s)
        ON CONFLICT (phone)
        DO UPDATE SET username = EXCLUDED.username
        """, (name, phone))
    
    conn.commit()
    print("Added or updated")


def show_all_contacts():
    cur.execute("SELECT * FROM phonebook")
    rows = cur.fetchall()

    print("\nAll contacts:")
    for row in rows:
        print(row)


def search_by_username():
    name = input("Enter username to search: ").strip()

    cur.execute(
        "SELECT * FROM phonebook WHERE username = %s",
        (name,)
    )
    rows = cur.fetchall()

    print("\nSearch result: ")
    for row in rows:
        print(row)


def search_by_phone_prefix():
    prefix_input = input("Enter phone prefix: ").strip()
    prefix = normalize_phone(prefix_input) if len(prefix_input) >= 11 else None

    if prefix is not None:
        search_value = prefix + "%"
    else:
        cleaned = re.sub(r"[^\d+]", "", prefix_input)
        if cleaned.startswith("8"):
            cleaned = "+7" + cleaned[1:]
        search_value = cleaned + "%"

    cur.execute(
        "SELECT * FROM phonebook WHERE phone LIKE %s",
        (search_value,)
    )
    rows = cur.fetchall()

    print("\nSearch result: ")
    for row in rows:
        print(row)


def update_contact():
    name = input("Enter username to update: ").strip()
    new_phone_input = input("Enter new phone (+7XXXXXXXXXX or 8XXXXXXXXXX): ").strip()

    new_phone = normalize_phone(new_phone_input)

    if new_phone is None:
        print("Invalid phone format. Use +7XXXXXXXXXX or 8XXXXXXXXXX")
        return
    
    try:
        cur.execute(
            "UPDATE phonebook SET phone = %s WHERE username = %s",
            (new_phone, name)
        )
        conn.commit()
        print("Updated")
    except Exception as e:
        conn.rollback()
        print("Error:", e)


def delete_by_username():
    name = input("Enter username to delete: ").strip()

    cur.execute(
        "DELETE FROM phonebook WHERE username = %s",
        (name,)
    )
    conn.commit()
    print("Deleted by username")


def delete_by_phone():
    phone_input = input("Enter phone to delete: ").strip()
    phone = normalize_phone(phone_input)

    if phone is None:
        print("Invalid phone format")
        return
    
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

        choice = input("Choose an option: ").strip()

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