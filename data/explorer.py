from .init import curs, IntegrityError
from model.explorer import Explorer
from error import Missing, Duplicate

curs.execute(
    """CREATE TABLE IF NOT EXISTS explorer(
    name text primary key,
    country text,
    description text
)"""
)


def row_to_model(row: tuple) -> Explorer:
    name, country, description = row
    return Explorer(name=name, country=country, description=description)


def model_to_dict(explorer: Explorer) -> dict:
    return explorer.dict()


def get_one(name: str) -> Explorer:
    qry = "SELECT * FROM explorer WHERE name=:name"
    params = {"name": name}
    curs.execute(qry, params)
    row = curs.fetchone()
    if row:
        return row_to_model(row)
    else:
        raise Missing(msg=f"Explorer {name} not found")


def get_all() -> list[Explorer]:
    qry = "SELECT * FROM explorer"
    curs.execute(qry)
    rows = curs.fetchall()
    return [row_to_model(row) for row in rows]


def create(explorer: Explorer) -> Explorer:
    if not explorer:
        return None
    qry = """INSERT INTO explorer (name,country,description)
    VALUES(:name,:country,:description)"""
    params = model_to_dict(explorer)
    try:
        curs.execute(qry, params)
        curs.connection.commit()
    except IntegrityError:
        raise Duplicate(msg=f"Explorer {explorer.name} already exists")
    return get_one(explorer.name)


def modify(name: str, explorer: Explorer) -> Explorer:
    if not (name and explorer):
        return None
    qry = """UPDATE Explorer
    SET name=:name,
    country=:country,
    description=:description
    WHERE name=:name_orig
    """
    params = model_to_dict(explorer)
    params["name_orig"] = explorer.name
    curs.execute(qry, params)
    if curs.rowcount == 1:
        curs.connection.commit()
        return get_one(explorer.name)
    else:
        raise Missing(msg=f"Explorer {name} not found")


def delete(name: str):  # -> bool:
    if not name:
        return False
    qry = "DELETE FROM explorer WHERE name=:name"
    params = {"name": name}
    curs.execute(qry, params)
    # res = curs.execute(qry, params)
    if curs.rowcount == 1:
        curs.connection.commit()
    else:
        raise Missing(msg=f"Explorer {name} not found")
    # return bool(res)
