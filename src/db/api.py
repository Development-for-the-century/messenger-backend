from typing import Annotated

from fastapi import APIRouter, Depends
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from db.core import Base, UserAddSchema, UserModel, UserSchema, engine, get_session

router = APIRouter(tags=["Database"], prefix="/db")


@router.post("/setup_database")
async def setup_database():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)
        await conn.run_sync(Base.metadata.create_all)

    return {"state": True}


@router.post("/add_user")
async def add_books(
    data: UserAddSchema,
    session: Annotated[AsyncSession, Depends(get_session)],
):
    new_user = UserModel(sub=data.sub, email=data.email)

    session.add(new_user)
    await session.commit()
    return {"state": True}


@router.get("/get_user")
async def get_books(
    data: UserSchema,
    session: Annotated[AsyncSession, Depends(get_session)],
):
    query = select(UserModel)
    result = await session.execute(query)
    return result.scalars().all()
