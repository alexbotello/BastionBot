from sqlalchemy import create_engine, Column, String
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()


def db_connect():
    """
    Performs database connection
    Returns sqlalchemy engine instance
    """
    return create_engine('postgres://fcvxvbdsuotypy:a3b010cca1fa4e6949ff39c11c6'
                         'e0b9edf9ce67a650535436dc349ba29b8c751@ec2-54-243-253-'
                         '17.compute-1.amazonaws.com:5432/'
                         'dfl66jjoa0etqc', echo=False)


def create_battletag_table(engine):

    Base.metadata.create_all(engine)


class Battletags(Base):
    """
    Table to store user battletags
    """
    __tablename__ = 'Battletags'

    disc_name = Column(String, primary_key=True)
    battletag = Column(String, unique=True)
