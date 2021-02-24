from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os
from dotenv import find_dotenv, load_dotenv

load_dotenv(find_dotenv())

SQLACHEMY_DATABASE_URL = os.getenv('DATABASE_URL_LOCAL')
engine = create_engine(SQLACHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
