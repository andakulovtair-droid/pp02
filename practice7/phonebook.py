import csv
from connect import connect


def create_table():
    conn = connect()
    cur = conn.cursor()

    cur.execute("""
        CREATE TABLE IF NOT EXISTS phonebook (
            name VARCHAR(100) PRIMARY KEY,
            phone VARCHAR(20) UNIQUE NOT NULL
        )
    """)

    conn.commit()
    cur.close()
    conn.close()
    print("Table created")

def insert_console():
    name = input("Name: ").strip()
    phone = input("Phone: ").strip()

    conn = connect()
    cur = conn.cursor()

    try:
        cur.execute(
            "INSERT INTO phonebook (name, phone) VALUES (%s, %s)",
            (name, phone)
        )
        conn.commit()
        print("Inserted")
    except Exception as e:
        conn.rollback()
        print("Error:", e)

    cur.close()
    conn.close()


def import_from_csv():
    filename = input("CSV file name: ").strip()

    conn = connect()
    cur = conn.cursor()

    try:
        with open(filename, "r", encoding="utf-8") as file:
            reader = csv.DictReader(file)

            for row in reader:
                name = row["name"].strip()
                phone = row["phone"].strip()

                try:
                    cur.execute(
                        "INSERT INTO phonebook (name, phone) VALUES (%s, %s) "
                        "ON CONFLICT (phone) DO NOTHING",
                        (name, phone)
                    )
                except:
                    pass

        conn.commit()
        print("CSV imported")
    except Exception as e:
        conn.rollback()
        print("Error:", e)

    cur.close()
    conn.close()


def show_all():
    conn = connect()
    cur = conn.cursor()

    cur.execute("SELECT name, phone FROM phonebook ORDER BY name")
    rows = cur.fetchall()

    if rows:
        for row in rows:
            print(row)
    else:
        print("No contacts found")

    cur.close()
    conn.close()


def update_contact():
    old_name = input("Enter current name of contact: ").strip()

    conn = connect()
    cur = conn.cursor()

    cur.execute("SELECT * FROM phonebook WHERE name = %s", (old_name,))
    person = cur.fetchone()

    if not person:
        print("Contact not found")
        cur.close()
        conn.close()
        return

    print("1. Update name")
    print("2. Update phone")
    choice = input("Choose: ").strip()

    if choice == "1":
        new_name = input("New name: ").strip()
        cur.execute(
            "UPDATE phonebook SET name = %s WHERE name = %s",
            (new_name, old_name)
        )
        print("Name updated")

    elif choice == "2":
        new_phone = input("New phone: ").strip()
        try:
            cur.execute(
                "UPDATE phonebook SET phone = %s WHERE name = %s",
                (new_phone, old_name)
            )
            print("Phone updated")
        except Exception as e:
            conn.rollback()
            print("Error:", e)
            cur.close()
            conn.close()
            return
    else:
        print("Wrong choice")
        cur.close()
        conn.close()
        return

    conn.commit()
    cur.close()
    conn.close()


def query_contacts():
    print("1. Search by name")
    print("2. Search by phone")
    print("3. Search by name pattern")
    choice = input("Choose: ").strip()

    conn = connect()
    cur = conn.cursor()

    if choice == "1":
        name = input("Enter name: ").strip()
        cur.execute("SELECT * FROM phonebook WHERE name = %s", (name,))

    elif choice == "2":
        phone = input("Enter phone: ").strip()
        cur.execute("SELECT * FROM phonebook WHERE phone = %s", (phone,))

    elif choice == "3":
        pattern = input("Enter pattern: ").strip()
        cur.execute(
            "SELECT * FROM phonebook WHERE name ILIKE %s",
            ('%' + pattern + '%',)
        )
    else:
        print("Wrong choice")
        cur.close()
        conn.close()
        return

    rows = cur.fetchall()

    if rows:
        for row in rows:
            print(row)
    else:
        print("Nothing found")

    cur.close()
    conn.close()


def delete_contact():
    print("1. Delete by name")
    print("2. Delete by phone")
    choice = input("Choose: ").strip()

    conn = connect()
    cur = conn.cursor()

    if choice == "1":
        name = input("Enter name: ").strip()
        cur.execute("DELETE FROM phonebook WHERE name = %s", (name,))
        print("Deleted by name")

    elif choice == "2":
        phone = input("Enter phone: ").strip()
        cur.execute("DELETE FROM phonebook WHERE phone = %s", (phone,))
        print("Deleted by phone")

    else:
        print("Wrong choice")
        cur.close()
        conn.close()
        return

    conn.commit()
    cur.close()
    conn.close()


def main():
    while True:
        print("\n--- PHONEBOOK MENU ---")
        print("1. Create table")
        print("2. Insert from console")
        print("3. Import from CSV")
        print("4. Show all contacts")
        print("5. Update contact")
        print("6. Search contacts")
        print("7. Delete contact")
        print("0. Exit")

        choice = input("Choose: ").strip()

        if choice == "1":
            create_table()
        elif choice == "2":
            insert_console()
        elif choice == "3":
            import_from_csv()
        elif choice == "4":
            show_all()
        elif choice == "5":
            update_contact()
        elif choice == "6":
            query_contacts()
        elif choice == "7":
            delete_contact()
        elif choice == "0":
            print("Bye")
            break
        else:
            print("Wrong choice")


main()