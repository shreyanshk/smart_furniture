from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, scoped_session

engine = create_engine('sqlite:////tmp/iotdb.sqlite3')
Base = declarative_base()
Session = scoped_session(sessionmaker(bind=engine))


class Event(Base):
	__tablename__ = "events"
	id = Column(Integer, primary_key=True)
	eventtype = Column(String, nullable=False)
	event = Column(String, nullable=False)
	deviceid = Column(String, nullable=False)
	timestamp = Column(DateTime, nullable=False)

	def __init__(self, **kwargs):
		self.eventtype = kwargs['eventtype']
		self.event = kwargs['event']
		self.deviceid = kwargs['deviceid']
		self.timestamp = kwargs['timestamp']

	def as_dict(self):
		return {
			'eventtype': self.eventtype,
			'event': self.event,
			'deviceid': self.deviceid,
			'timestamp': str(self.timestamp),
		}


class User(Base):
	__tablename__ = 'users'
	id = Column(Integer, primary_key=True)
	username = Column(String, nullable=False)
	pwhash = Column(String, nullable=False)
	deviceid = Column(String, nullable=False)

	def __init__(self, **kwargs):
		self.username = kwargs['username']
		self.pwhash = kwargs['pwhash']
		self.deviceid = kwargs['deviceid']


def initialize_db():
	Base.metadata.drop_all(engine)
	Base.metadata.create_all(engine)
	print('initialized db tables')
