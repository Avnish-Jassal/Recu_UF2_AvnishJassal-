def user_schema(user) -> dict:
    return {"id" : [0],
            "nom" : [1],
            "email" : [2],
            "descripcio": [3],
            "curs": [4],
            "any" : [5],
            "dirrecio" : [6],
            "codi_postal": [7],
            "password" : [8]
            }

def users_schemas(users) -> list[dict]:
    return [users_schemas(u) for u in users]
