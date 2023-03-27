from fastapi import APIRouter, Depends
from sqlalchemy import select, delete
from sqlalchemy.ext.asyncio import AsyncSession

from app.db.database import get_session
from app.idiom.model import Idiom
from app.idiom.schema import IdiomCreate

idiom_router = APIRouter(prefix="/api/idiom")


@idiom_router.get('/')
async def get_idioms(db: AsyncSession = Depends(get_session)):
    idioms = await db.execute(select(Idiom))
    return idioms.scalars().fetchall()


@idiom_router.get('/init')
async def init_matcher(db: AsyncSession = Depends(get_session)):
    idioms = await db.execute(select(Idiom))
    result = idioms.scalars().all()
    from app.main import matcher
    matcher.init(result)


@idiom_router.post("/")
async def create_idioms(req: IdiomCreate, db: AsyncSession = Depends(get_session)):
    idiom = Idiom(**req.dict())
    await idiom.save(db)
    return idiom


@idiom_router.get("/search/{meaning}")
async def search_idioms(meaning):
    from app.main import matcher
    return matcher.find(meaning)


@idiom_router.delete("/{id}")
async def delete_idiom(id, db: AsyncSession = Depends(get_session)):
    idiom = await db.execute(delete(Idiom).where(Idiom.id == int(id)))
    await db.commit()
    return idiom
