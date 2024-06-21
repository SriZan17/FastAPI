from model.creature import Creature

_creatures: list[Creature] = [
    Creature(
        name="yeti",
        country="CN",
        area="Himalayas",
        description="Hirsute Himalayan",
        aka="Abominable Snowman",
    ),
    Creature(
        name="sasquatch",
        country="US",
        area="*",
        description="Yeti's Cousin Eddie",
        aka="Bigfoot",
    ),
    Creature(
        name="Pheonix",
        country="Arizona",
        area="NA",
        description="Risen from its ashes",
        aka="Burning Bird",
    ),
]


def get_all() -> list[Creature]:
    return _creatures


def get_one(name: str) -> Creature | None:
    for _creature in _creatures:
        if _creature.name == name:
            return _creature
    return None


def create(creature: Creature) -> Creature:
    return creature


def modify(name: str, creature: Creature) -> Creature:
    return creature


def replace(crature: Creature) -> Creature:
    return crature


def delete(name: str):
    return None
