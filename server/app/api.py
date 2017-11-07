import hashlib
from datetime import datetime

from flask import Blueprint, request
from flask_sqlalchemy_session import current_session

from .dbmodels import Event, User
import json


api = Blueprint('api', __name__)


@api.route('/api/record_event', methods=['POST'])
def record_event():
	data = json.loads(request.data)
	try:
		event = data['event']
		eventtype = data['eventtype']
		deviceid = data['deviceid']
		timestamp = data['timestamp']
	except KeyError as e:
		return '', 404
	timestamp = datetime.strptime(timestamp, "%Y-%m-%d %H:%M:%S.%f")
	event = Event(event=event, eventtype=eventtype, timestamp=timestamp, deviceid=deviceid)
	current_session.add(event)
	current_session.commit()
	return '', 200


@api.route('/api/user_events', methods=['GET'])
def return_user_events():
	try:
		deviceid = request.values.get('deviceid')
	except KeyError:
		return "invalid request", 404
	data = current_session.query(Event).filter(
		Event.deviceid == deviceid,
	).all()
	data = [record.as_dict() for record in data]
	data = json.dumps(data)
	return data, 200


@api.route('/api/user_mgmt/add_user', methods=['POST'])
def add_user_to_system():
	try:
		username = request.values['username']
		password = request.values['password']
		deviceid = request.values['deviceid']
	except KeyError:
		return "invalid request", 404
	pwhash = hashlib.sha512(password).hexdigest()
	userrecord = User(username=username, pwhash=pwhash, clientid=deviceid)
	current_session.add(userrecord)
	current_session.commit()
	return '', 200
