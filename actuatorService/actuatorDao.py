import datatime
from sqlalchemy import create_engine, Sequence, ForeignKey, Column, Integer, String, Float, DateTime, Boolean
from sqlalchemy_utils import create_database
from sqlaclhemy.orm import sessionmaker, relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Actuator(Base):
    __tablename__ = "actuator"
    id = Column(Integer, Sequence("aIdSeq"), primary_key=True)
    actuatorId = Column(Integer, nullable=False)
    actuatorType = Column(String(30), nullable=False)
    actuatorActive = Column(Boolean, nullable=False)

class Subscription(Base):
    __tablename__ = "subscription"
    id = Column(Integer, Sequence("subIdSeq"))
    actuatorId = Column(Integer, ForeignKey("actuator.id"), nullable=False)
    threshold = Column(Float, nullable=False)
    timestamp = Column(DateTime, default=datetime.datetime.utcnow)
    actuator = relationship(Actuator)

engine = create_engine("sqlite:///mysqlite.db")
Base.metadata.create_all(engine)