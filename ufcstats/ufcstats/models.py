from sqlalchemy import Column, Integer, String, Boolean, UniqueConstraint
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

def create_table(engine):
    Base.metadata.create_all(engine)


class Fighter(Base):
    __tablename__ = 'fighters'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    first_name = Column(String, nullable=False)
    last_name = Column(String, nullable=False)
    nickname = Column(String, nullable=True)
    weight = Column(String, nullable=True)
    height = Column(String, nullable=True)
    reach = Column(Integer, nullable=True)
    stance = Column(String, nullable=True)
    wins = Column(Integer, nullable=False)
    losses = Column(Integer, nullable=False)
    draws = Column(Integer, nullable=False)
    belt = Column(Boolean, nullable=False)

    __table_args__ = (UniqueConstraint('first_name', 'last_name', name='fighter_unique_constraint'),)


class Event(Base):
    __tablename__ = 'events'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    date = Column(String, nullable=False)

    __table_args__ = (UniqueConstraint('name', 'date', name='event_unique_constraint'),)