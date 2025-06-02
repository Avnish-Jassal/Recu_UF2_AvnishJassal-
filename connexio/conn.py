import psycopg2

def connection_db():
    conn = psycopg2.connect(
    database = "Fastapi",
    password = "ITIC",
    user = "ITIC_user",
    host = "localhost",
    port = "5432"
    )
    return conn