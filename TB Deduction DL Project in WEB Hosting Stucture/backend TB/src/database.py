from sqlalchemy import MetaData
from sqlalchemy.ext.declarative import declarative_base
from .config import settings
from databases import Database


metadata = MetaData()
Base = declarative_base()


DATABASE_URL = settings.DATABASE_URL
database = Database(DATABASE_URL)
