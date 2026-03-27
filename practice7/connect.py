import psycopg2
import config

def connect():
    conn = psycopg2.connect(
        host=config.host,
        dbname=config.dbname,
        user=config.user,
        password=config.password,
        port=config.port
    )
    return conn