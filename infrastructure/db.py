from sqlalchemy import create_engine, URL
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv, dotenv_values
from infrastructure.models.base import Base

load_dotenv()
config = dotenv_values(".env")

USERNAME = config.get('DATABASE_USER')
PASSWORD = config.get('DATABASE_PASSWORD')
HOST = config.get('DATABASE_HOST')
DATABASE_NAME = config.get('DATABASE_NAME')
PORT = config.get('DATABASE_PORT')

DATABASE_URL = URL.create(
    "mysql+mysqlconnector",
    username=USERNAME,
    password=PASSWORD,
    host=HOST,
    database=DATABASE_NAME,
    port=PORT
)

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def init_db():
    Base.metadata.create_all(bind=engine)
