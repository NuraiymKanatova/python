from connect import connect
import re

conn = connect()
cur = conn.cursor()


def normalize_phone(phone):
    phone = phone.strip()
    # убираем пробелы, дефисы, скобки
    phone = re.sub(r"[^\d+]", "", phone)

    # формат 8701XXXXXXX -> +7701XXXXXXX
    if re.fullmatch(r"8\d{10}", phone):
        return "+7" + phone[1:]

    # формат +7701XXXXXXX
    if re.fullmatch(r"\+7\d{10}", phone):
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


def search_contacts():
    pattern = input("Enter search pattern: ").strip()

    cur.execute(
        "SELECT * FROM search_contacts(%s)",
        (pattern,)
    )
    rows = cur.fetchall()

    print("\nSearch result:")
    if not rows:
        print("No matches found")
    else:
        for row in rows:
            print(row)


def insert_or_update_user():
    name = input("Enter name: ").strip()
    phone_input = input("Enter phone (+7XXXXXXXXXX or 8XXXXXXXXXX): ").strip()

    phone = normalize_phone(phone_input)

    if phone is None:
        print("Invalid phone format. Use +7XXXXXXXXXX or 8XXXXXXXXXX")
        return

    cur.execute(
        "CALL insert_or_update_user(%s, %s)",
        (name, phone)
    )
    conn.commit()
    print("Added or updated")

def insert_many_users():
    try:
        count = int(input("How many users do you want to add? ").strip())
    except ValueError:
        print("Invalid number")
        return

    if count <= 0:
        print("Count must be greater than 0")
        return

    usernames = []
    phones = []

    for i in range(count):
        print(f"\nUser #{i + 1}")
        name = input("Enter name: ").strip()
        phone_input = input("Enter phone (+7XXXXXXXXXX or 8XXXXXXXXXX): ").strip()

        normalized_phone = normalize_phone(phone_input)

        usernames.append(name)
        phones.append(normalized_phone if normalized_phone is not None else phone_input.strip())

    cur.execute(
        "SELECT insert_many_users(%s::TEXT[], %s::TEXT[])",
        (usernames, phones)
    )

    result = cur.fetchone()
    conn.commit()

    invalid_data = result[0] if result and result[0] else ""

    print("\nBulk insert finished")
    if invalid_data:
        print("Invalid data found:")
        print(invalid_data)
    else:
        print("All users inserted/updated successfully")

def show_paginated_contacts():
    try:
        limit = int(input("Enter limit: ").strip())
        offset = int(input("Enter offset: ").strip())
    except ValueError:
        print("Limit and offset must be integers")
        return

    cur.execute(
        "SELECT * FROM get_contacts_paginated(%s, %s)",
        (limit, offset)
    )
    rows = cur.fetchall()

    print("\nPaginated contacts:")
    if not rows:
        print("No contacts found")
    else:
        for _, username, phone in rows:
            print(username, phone)


def delete_contact():
    value = input("Enter username or phone to delete: ").strip()

    normalized = normalize_phone(value)
    if normalized is not None:
        value = normalized

    cur.execute(
        "CALL delete_contact_by_value(%s)",
        (value,)
    )
    conn.commit()
    print("Deleted")


def menu():
    create_table()

    while True:
        print("\n--- PHONEBOOK MENU ---")
        print("1. Search contacts by pattern")
        print("2. Insert or update one user")
        print("3. Insert many users")
        print("4. Show paginated contacts")
        print("5. Delete contact by username or phone")
        print("0. Exit")

        choice = input("Choose an option: ").strip()

        if choice == "1":
            search_contacts()
        elif choice == "2":
            insert_or_update_user()
        elif choice == "3":
            insert_many_users()
        elif choice == "4":
            show_paginated_contacts()
        elif choice == "5":
            delete_contact()
        elif choice == "0":
            break
        else:
            print("Invalid choice")


menu()

cur.close()
conn.close()
print("Connection closed")