from fastapi import APIRouter, Depends
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.db.database import get_session
from app.idiom.model import Idiom
from app.idiom.schema import IdiomCreate

idiom_router = APIRouter(prefix="/api/idiom")


@idiom_router.get('/')
async def get_idioms(db: AsyncSession = Depends(get_session)):
    idioms = await db.execute(select(Idiom))
    return idioms.scalars().fetchall()


@idiom_router.post("/")
async def create_idioms(req: IdiomCreate, db: AsyncSession = Depends(get_session)):
    print('req', req)
    idiom = Idiom(**req.dict())
    print('idiom', idiom)
    await idiom.save(db)
    return idiom
