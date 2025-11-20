import os
from dotenv import load_dotenv
from sqlalchemy import (
    create_engine, URL, MetaData,
)

load_dotenv()


class Config:
    DB_USER = os.getenv('DB_USER')
    DB_PASS = os.getenv('DB_PASS')
    DB_NAME = os.getenv('DB_NAME')
    DB_HOST = os.getenv('DB_HOST')
    DB_PORT = os.getenv('DB_PORT')

config = Config()

url = URL.create(
    drivername='postgresql+psycopg2',
    username=config.DB_USER,
    password=config.DB_PASS,
    host=config.DB_HOST,
    port=config.DB_PORT,
    database=config.DB_NAME
)
engine = create_engine(url)
metadata_obj = MetaData()
