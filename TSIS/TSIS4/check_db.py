import pg8000.native

PASSWORD = "710710Aktakt_"  # <-- замени

# Без try/except чтобы увидеть полный traceback
conn = pg8000.native.Connection(
    host="localhost",
    port=5432,
    database="snake_db",
    user="postgres",
    password=PASSWORD,
)
print("OK!")
conn.close()