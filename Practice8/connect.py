import psycopg
from config import load_config

def connect():
    config = load_config()

    conn = psycopg.connect(
        host=config["host"],
        port=config["port"],
        dbname=config["dbname"],
        user=config["user"],
        password=config["password"]
    )

    return conn