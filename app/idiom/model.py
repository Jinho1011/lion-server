from sqlalchemy import Column, Integer, String, Text

from app.db.base import Base


class Idiom(Base):
    __tablename__ = "idiom"

    id = Column(Integer, primary_key=True, autoincrement=True)
    hanja = Column(String, nullable=False, unique=True)  # 故事成語
    hangeul = Column(Text, nullable=False)  # 고사성어
    meaning = Column(String, nullable=False)  # 고사에서 유래된 한자어 관용어
