import datetime
from sqlalchemy import ForeignKey, Column, Integer, Double, DateTime, Sequence
from sqlalchemy.orm import relationship

class DataPoint(Base):

    __tablename__ = 'datapoints'

    id = Column(Integer, Sequence('dpSeqId') primary_key=True)
    sensorId = Column(Integer, ForeignKey('sensor.id'))
    value = Column(Double)
    timestamp = Column(DateTime, default=datetime.datetime.utcnow)

    sensor = relationship('Sensor', back_populates='datapoints')

    def __init__(self, sId, value, timestamp):
        self.sensorId = sId
        self.value = value
        self.timestamp = timestamp

    def __repr__(self):
        return '<DataPoint(id={self.sensorId!r} value={self.value!r} timestamp={self.timestamp})>'.format(self=self)

    
