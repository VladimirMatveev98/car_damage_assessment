import asyncio

from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession
from sqlalchemy.orm import Session, sessionmaker
from sqlalchemy import URL, create_engine, text
from config import settings


engine = create_engine(
         url=settings.database_url_psycopg,
         echo=False
         )

async_engine = create_async_engine(
    url=settings.database_url_asyncpg,
    echo=False
)


async def test_async_connection():
    async with async_engine.connect() as conn:
        answer = await conn.execute(text("SELECT VERSION()"))
        print(f"{answer.all()=}")


def test_connection():
    with engine.connect() as c:
        answer = c.execute(text("SELECT VERSION()"))
        print(f"{answer.all()=}")


# Проверка асинхронного соединения:
print("Проверка асинхронного подключения: ")
asyncio.run(test_async_connection())

# Проверка синхронного подключения
print("Проверка синхронного подключения: ")
test_connection()



