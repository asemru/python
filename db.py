from sqlalchemy.orm import DeclarativeBase, sessionmaker
from sqlalchemy import create_engine

ending = create_engine('sqlite:///taskmanager.db')
SessionLocal = sessionmaker(bind=ending)


class Base(DeclarativeBase):
    pass