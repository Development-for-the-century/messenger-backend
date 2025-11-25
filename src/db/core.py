from pydantic import BaseModel
from sqlalchemy.ext.asyncio import async_sessionmaker, create_async_engine
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column

from app.config import get_db_settings

db_settings = get_db_settings()

engine = create_async_engine(db_settings.DSN.unicode_string())
new_session = async_sessionmaker(engine)


async def get_session():
    async with new_session() as session:
        yield session


class Base(DeclarativeBase):
    pass


class UserModel(Base):
    __tablename__ = "user"

    id: Mapped[int] = mapped_column(primary_key=True)
    sub = Mapped[str]
    email = Mapped[str]


class UserAddSchema(BaseModel):
    sub: str
    email: str


class UserSchema(UserAddSchema):
    id: int
