from os import environ

from dotenv import load_dotenv
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession

from app.db import Base

load_dotenv(verbose=True)

SQLALCHEMY_DATABASE_URL = environ['DB_URL']

engine = create_async_engine(SQLALCHEMY_DATABASE_URL)


async def get_session():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

    session = AsyncSession(bind=engine)
    try:
        yield session
    finally:
        await session.close()
