from connexio.conn import connection_db


def register_user():
    conn = connection_db()
    cursor = conn.cursor()
    cursor.execute("""INSERT INTO clients (nom, cognom, email, descripcio, curs, any, dirrecio, codi_postal, password
                    VALUES (%s, %s, %s,%s, %s, %s, %s, %s, %s )"""
    )
    result = cursor.fetchall()
    conn.commit()
    cursor.close()
    conn.close()

    return result
