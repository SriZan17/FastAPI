from model.creature import Creature
import pytest
from error import Missing, Duplicate
from data import creature as data
import os

os.environ["CRYPTID_UNIT_TEST"] = "true"


@pytest.fixture
def sample() -> Creature:
    return Creature(
        name="yeti",
        country="CN",
        area="Himalayas",
        description="Handsome Himalayan",
        aka="Abominable Snowman",
    )


def test_create(sample):
    resp = data.create(sample)
    assert resp == sample


def test_create_duplicate(sample):
    resp = data.create(sample)
    assert resp == sample
    with pytest.raises(Duplicate):
        resp = data.create(sample)


def test_get_exists(sample):
    resp = data.create(sample)
    assert resp == sample
    resp = data.get_one(sample.name)
    assert resp == sample


def test_get_missing():
    with pytest.raises(Missing):
        _ = data.get_one("boxturtle")


def test_modify(sample):
    sample.country = "CA"
    resp = data.modify(sample.name, sample)
    assert resp == sample


def test_modify_missing():
    bob: Creature = Creature(
        name="bob", country="US", area="*", description="some guy", aka="??"
    )
    with pytest.raises(Missing):
        _ = data.modify(bob.name, bob)
