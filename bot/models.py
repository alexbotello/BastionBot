from sqlalchemy import create_engine, Column, String
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()


def db_connect():
    """
    Performs database connection
    Returns sqlalchemy engine instance
    """
    return create_engine('postgres://avvcurseaphtxf:X0466JySVtLq6nyq_5pb7BQNjR@'
                         'ec2-54-227-250-80.compute-1.amazonaws.com'
                         ':5432/d7do67r1b7t1nn', echo=False)


def create_battletag_table(engine):

    Base.metadata.create_all(engine)


class Battletags(Base):
    """
    Table to store user battletags
    """
    __tablename__ = 'Battletags'

    disc_name = Column(String, primary_key=True)
    battletag = Column(String, unique=True)
