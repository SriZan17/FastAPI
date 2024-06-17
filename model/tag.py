from datetime import datetime
from pydantic import BaseClass


class TagIn(BaseClass):
    tag: str


class Tag(BaseClass):
    tag: str
    created: datetime
    secrect: str


class TagOut(BaseClass):
    tag: str
    created: datetime
