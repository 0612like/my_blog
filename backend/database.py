import os
from sqlalchemy import create_engine, MetaData
from databases import Database

DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///./blog.db")

# SQLAlchemy engine (同步操作，主要用于 Alembic 或初始化)
engine = create_engine(DATABASE_URL)

metadata = MetaData()

# Databases (异步操作)
database = Database(DATABASE_URL) 