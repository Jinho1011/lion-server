from collections.abc import AsyncGenerator
from os import environ

from dotenv import load_dotenv
from fastapi.encoders import jsonable_encoder
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker

load_dotenv(verbose=True)

SQLALCHEMY_DATABASE_URL = environ['DB_URL']

engine = create_async_engine(SQLALCHEMY_DATABASE_URL, future=True,
                             echo=True,
                             json_serializer=jsonable_encoder, )

AsyncSessionFactory = sessionmaker(engine, autoflush=False, expire_on_commit=False, class_=AsyncSession)


async def get_session() -> AsyncGenerator:
    async with AsyncSessionFactory() as session:
        yield session
