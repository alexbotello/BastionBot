from sqlalchemy import create_engine, Column, String
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()


def db_connect():
    """
    Performs database connection
    Returns sqlalchemy engine instance
    """
    return create_engine('DB_URL_HERE', echo=False)


def create_battletag_table(engine):

    Base.metadata.create_all(engine)


class Battletags(Base):
    """
    Table to store user battletags
    """
    __tablename__ = 'Battletags'

    disc_name = Column(String, primary_key=True)
    battletag = Column(String, unique=True)
