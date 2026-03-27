import csv
from connect import connect

def create_table():
    conn = connect()
    cur = conn.cursor()
    cur.execute("""
        CREATE TABLE IF NOT EXISTS phonebook (
            id SERIAL PRIMARY KEY,
            name VARCHAR(50),
            phone VARCHAR(20)
        )
    """)
    conn.commit()
    cur.close()
    conn.close()

def insert_console():
    name = input("Name: ")
    phone = input("Phone: ")

    conn = connect()
    cur = conn.cursor()
    cur.execute("INSERT INTO phonebook (name, phone) VALUES (%s, %s)", (name, phone))
    conn.commit()
    cur.close()
    conn.close()

def insert_csv():
    conn = connect()
    cur = conn.cursor()

    with open("contacts.csv", "r", encoding="utf-8") as f:
        reader = csv.reader(f)
        next(reader)
        for row in reader:
            cur.execute("INSERT INTO phonebook (name, phone) VALUES (%s, %s)", (row[0], row[1]))

    conn.commit()
    cur.close()
    conn.close()

def show():
    conn = connect()
    cur = conn.cursor()
    cur.execute("SELECT * FROM phonebook")
    for row in cur.fetchall():
        print(row)
    cur.close()
    conn.close()

def update():
    old_name = input("Old name: ")
    new_phone = input("New phone: ")

    conn = connect()
    cur = conn.cursor()
    cur.execute("UPDATE phonebook SET phone=%s WHERE name=%s", (new_phone, old_name))
    conn.commit()
    cur.close()
    conn.close()

def delete():
    name = input("Name: ")

    conn = connect()
    cur = conn.cursor()
    cur.execute("DELETE FROM phonebook WHERE name=%s", (name,))
    conn.commit()
    cur.close()
    conn.close()

create_table()

while True:
    print("\n1-add 2-csv 3-show 4-update 5-delete 0-exit")
    n = input("Choose: ")

    if n == "1":
        insert_console()
    elif n == "2":
        insert_csv()
    elif n == "3":
        show()
    elif n == "4":
        update()
    elif n == "5":
        delete()
    elif n == "0":
        break