import datetime
from sqlalchemy import create_engine, Sequence, ForeignKey, Column, Integer, String, Float, DateTime, Boolean
from sqlalchemy_utils import create_database
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Actuator(Base):
    __tablename__ = "actuator"
    id = Column(Integer, Sequence("aIdSeq"), primary_key=True)
    actuatorId = Column(Integer, nullable=False)
    actuatorType = Column(String(30), nullable=False)
    actuatorActive = Column(Boolean, nullable=False)


class Rule(Base):
    __tablename__ = "rules"
    id = Column(Integer, Sequence("subIdSeq"), primary_key=True)
    actuatorId = Column(Integer, ForeignKey("actuator.id"), nullable=False)
    sensorType = Column(String(30), nullable=False)
    sensorId = Column(Integer, nullable=False)
    threshold = Column(Float, nullable=False)
    timestamp = Column(DateTime, default=datetime.datetime.utcnow)
    gt = Column(Boolean, nullable=False)
    actuator = relationship(Actuator)


engine = create_engine("sqlite:///mysqlite.db")
Base.metadata.create_all(engine)
