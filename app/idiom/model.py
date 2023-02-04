from sqlalchemy import Column, Integer, String, Text, DateTime, Table

from app.db import Base


class Idiom(Base):
    __tablename__ = "idiom"

    id = Column(Integer, primary_key=True, autoincrement=True)
    hanja = Column(String, nullable=False)  # 故事成語
    hangeul = Column(Text, nullable=False)  # 고사성어
    meaning = Column(String, nullable=False)  # 고사에서 유래된 한자어 관용어
