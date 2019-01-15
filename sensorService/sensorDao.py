import datetime
from sqlalchemy import create_engine, Sequence, ForeignKey, Column, Integer, String, Float, DateTime
#from sqlalchemy_utils import create_database
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Sensor(Base):
    __tablename__ = 'sensor'
    id = Column(Integer, Sequence('sIdSeqId'), primary_key=True)
    sensorId = Column(Integer, nullable=False)
    sensorType = Column(String(30), nullable=False)

class DataPoint(Base):
    __tablename__ = 'datapoint'
    id = Column(Integer, Sequence('dpSeqId'), primary_key=True)
    sensorId = Column(Integer, ForeignKey('sensor.sensorId'), nullable=False)
    value = Column(Float, nullable=False)
    timestamp = Column(DateTime, default=datetime.datetime.utcnow)
    sensor = relationship(Sensor)

engine = create_engine("sqlite:///mysqlite.db")

Base.metadata.create_all(engine)
