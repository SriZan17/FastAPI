from model.explorer import Explorer

_explorers = [
    Explorer(
        name="Claude",
        country="FR",
        description="Full moon nightmare",
    ),
    Explorer(
        name="Noah",
        country="DE",
        description="Machete man",
    ),
]


def get_all() -> list[Explorer]:
    return _explorers


def get_one(name: str) -> Explorer | None:
    for _explorer in _explorers:
        if _explorer.name == name:
            return _explorer
    return None


def create(explorer: Explorer) -> Explorer:
    return explorer


def modify(name: str, explorer: Explorer) -> Explorer:
    return explorer


def replace(explorer: Explorer) -> Explorer:
    return explorer


def delete(name: str):
    return None
