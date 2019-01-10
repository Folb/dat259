from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Sensor(Base):
    __tablename__ = 'sensors'

    id = Column(Integer, Sequence('sIdSeqId'), primary_key=True)
    sensorType = Column(String)
    sensorId = Column(Integer)

    def __init__(self, sType, sid):
        self.sensorType = sType
        self.sensorId = sid

    def __repr__(self):
        return '<Sensor(type={self.sensorType!r} id={self.sensorId!r})>'.format(self=self)
