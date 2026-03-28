import psycopg
from config import load_config

def connect():
    config = load_config()

    conn = psycopg.connect(
        f"host={config['host']} "
        f"port={config['port']} "
        f"dbname={config['dbname']} "
        f"user={config['user']} "
        f"password={config['password']}"
    )

    return conn