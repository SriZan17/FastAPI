from model import Creature

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


def get_creatures() -> list[Creature]:
    return _creatures
