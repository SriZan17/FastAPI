# might have to make environment variable(remove quotes)
# CRYPTID_SQLITE_DATABASE = ":memory:"

import os
import pytest
from model.explorer import Explorer
from error import Missing, Duplicate
from data import explorer

os.environ["CRYPTID_SQLITE_DB"] = ":memory:"


@pytest.fixture
def sample() -> Explorer:
    return Explorer(name="Bill", country="CN", description="Shotgn Menace")


def test_create(sample):
    resp = explorer.create(sample)
    assert resp == sample


def test_create_duplicate(sample):
    with pytest.raises(Duplicate):
        _ = explorer.create(sample)


def test_get_one(sample):
    resp = explorer.get_one(sample.name)
    assert resp == sample


def test_get_one_missing():
    with pytest.raises(Missing):
        _ = explorer.get_one("sam")


def test_modify(sample):
    explorer.country = "FR"
    resp = explorer.modify(sample.name, sample)
    assert resp == sample


def test_modify_missing():
    thing: Explorer = Explorer(name="juan", country="ME", description="some thing")
    with pytest.raises(Missing):
        _ = explorer.modify(thing.name, thing)


def test_delete(sample):
    resp = explorer.delete(sample.name)
    assert resp is None


def test_delete_missing(sample):
    with pytest.raises(Missing):
        _ = explorer.delete(sample.name)
