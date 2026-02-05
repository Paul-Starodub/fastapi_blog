from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase, sessionmaker
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine, async_sessionmaker


class Base(DeclarativeBase):
    pass


######## async version sqlite ##########
SQLALCHEMY_DATABASE_URL = "sqlite+aiosqlite:///./blog.db"


engine = create_async_engine(
    SQLALCHEMY_DATABASE_URL,
    connect_args={"check_same_thread": False},
    echo=True,  # for debugging
)

AsyncSessionLocal = async_sessionmaker(
    bind=engine, class_=AsyncSession, expire_on_commit=False
)


async def get_db():
    async with AsyncSessionLocal() as session:
        yield session


######## sync version sqlite ##########
# SQLALCHEMY_DATABASE_URL = "sqlite:///./blog.db"
#
# engine = create_engine(
#     SQLALCHEMY_DATABASE_URL,
#     connect_args={"check_same_thread": False},
# )
#
# SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
#
# def get_db():
#     with SessionLocal() as db:
#         yield db
#
