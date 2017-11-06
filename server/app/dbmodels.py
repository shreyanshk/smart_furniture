from sqlalchemy import Column, Integer, String, TIMESTAMP
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, scoped_session

engine = create_engine('sqlite://')
Base = declarative_base()
Session = scoped_session(sessionmaker(bind=engine))


class Event(Base):
	__tablename__ = "iot_events"
	id = Column(Integer, primary_key=True)
	type = Column(String, nullable=False)
	event = Column(String, nullable=False)
	clientid = Column(String, nullable=False)
	timestamp = Column(TIMESTAMP, nullable=False)

	def __init__(self, **kwargs):
		self.type = kwargs['type']
		self.event = kwargs['event']
		self.clientid = kwargs['clientid']
		self.timestamp = kwargs['timestamp']

	def as_dict(self):
		return {
			'type': self.type,
			'event': self.event,
			'clientid': self.clientid,
			'timestamp': str(self.timestamp),
		}


def initialize_db():
	Base.metadata.drop_all(engine)
	Base.metadata.create_all(engine)
	print('reinitialized db tables')


if __name__ == '__main__':
	initialize_db()
