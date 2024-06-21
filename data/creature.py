from .init import curs, IntegrityError
from model.creature import Creature
from error import Missing, Duplicate

curs.execute(
    """CREATE TABLE IF NOT EXISTS creature(
    name text primary key,
    description text,
    country text,
    area text,
    aka text
    )"""
)


def row_to_model(row: tuple) -> Creature:
    name, description, country, area, aka = row
    return Creature(
        name=name, description=description, country=country, area=area, aka=aka
    )


def model_to_dict(creature: Creature) -> dict:
    return creature.dict()


def get_one(name: str) -> Creature:
    qry = "SELECT * FROM creature WHERE name=:name"
    params = {"name": name}
    curs.execute(qry, params)
    row = curs.fetchone()
    if row:
        return row_to_model(row)
    else:
        raise Missing(msg=f"Creature {name} not found")


def get_all() -> list[Creature]:
    qry = "SELECT * FROM creature"
    curs.execute(qry)
    # rows = list(curs.fetchall())
    rows = curs.fetchall()
    return [row_to_model(row) for row in rows]


def create(creature: Creature) -> Creature:
    if not creature:
        return None
    qry = """INSERT INTO creature
    (name, description, country, area, aka)
    VALUES (:name, :description, :country, :area, :aka)"""
    params = model_to_dict(creature)
    try:
        curs.execute(qry, params)
        curs.connection.commit()
        return get_one(creature.name)
    except IntegrityError:
        raise Duplicate(msg=f"Creature {creature.name} already exists")


def modify(name: str, creature: Creature) -> Creature:
    if not (name and creature):
        return None
    qry = """UPDATE creature SET
            country=:country,
            name=:name,
            description=:description,
            area=:area,
            aka=:aka WHERE name=:name_orig
            """
    params = model_to_dict(creature)
    params["name_orig"] = creature.name
    curs.execute(qry, params)
    if curs.rowcount == 1:
        curs.connection.commit()
        return get_one(creature.name)
    else:
        raise Missing(msg=f"Creature{name} not found")


# def modify(creature: Creature) -> Creature:
#    qry = """UPDATE creature SET
#            country=:country,
#            name=:name,
#            description=:description,
#            area=:area,
#            aka=:aka WHERRE name=:name_orig
#            """
#    params = model_to_dict(creature)
#    params["name_orig"] = creature.name
#    curs.execute(qry, params)
#    return get_one(creature.name)


def delete(name: str):
    if not name:
        return False
    qry = "DELETE FROM creature WHERE name=:name"
    params = {"name": name}
    curs.execute(qry, params)
    if curs.rowcount == 1:
        curs.connection.commit()
    else:
        raise Missing(msg=f"Creature {name} not found")
