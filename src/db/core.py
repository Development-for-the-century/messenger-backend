from sqlalchemy.ext.asyncio import async_sessionmaker, create_async_engine

from app.config import get_db_settings

db_settings = get_db_settings()
engine = create_async_engine(db_settings.DSN.unicode_string())

session = async_sessionmaker(engine)
