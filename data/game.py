from .init import curs


def get_word() -> str:
    qry = "SELECT name FROM creature ORDER BY RANDOM() LIMIT 1"
    curs.execute(qry)
    row = curs.fetchone()
    if row:
        name = row[0]
    else:
        name = "bigfoot"
    return name
