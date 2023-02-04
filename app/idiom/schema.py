from datetime import datetime

from pydantic import BaseModel


class IdiomCreate(BaseModel):
    hanja: str
    hangeul: str
    meaning: str
