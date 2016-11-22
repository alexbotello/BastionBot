from sqlalchemy import create_engine, Column, String
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()


def db_connect():
    """
    Performs database connection
    Returns sqlalchemy engine instance
    """
    return create_engine('postgres://fbcmeskynsvati:aURfAdENt6-kumO0j224GuXRWH'
                         '@ec2-54-221-235-135.compute-1.amazonaws.com'
                         ':5432/d2cc1tb2t1iges', echo=False)


def create_battletag_table(engine):

    Base.metadata.create_all(engine)


class Battletags(Base):
    """
    Table to store user battletags
    """
    __tablename__ = 'Battletags'

    disc_name = Column(String, primary_key=True)
    battletag = Column(String, unique=True)
