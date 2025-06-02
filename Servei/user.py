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

def get_user(user_id):
    conn = connection_db()
    cursor = conn.cursor()
    cursor.execute(""" SELECT id, nom, cognom, email, curs, any, direccio FROM clients WHERE id = %s """)
    result = cursor.fetchall()
    conn.commit()
    cursor.close()
    conn.close()

    return result

def update_user(id, cognom, dirrecio):
    conn = connection_db()
    cursor = conn.cursor()
    cursor.execute("""UPDATE clients SET cognom=%s, direccio=%s WHERE id=%s""")
    result = cursor.fetchall()
    conn.commit()
    cursor.close()
    conn.close()

    return result

def delete_user (id):
    conn = connection_db()
    cursor = conn.cursor()
    cursor.execute("""DELETE FROM clients WHERE id = %s,""")
    result = cursor.fetchall()
    conn.commit()
    cursor.close()
    conn.close()

    return result
