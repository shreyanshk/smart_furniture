from flask import Blueprint, request
from flask_sqlalchemy_session import current_session

from .dbmodels import Event
import json


api = Blueprint('api', __name__)


@api.route('/api/record_event', methods=['POST'])
def record_event():
	data = json.loads(request.data)
	print(data)
	event = Event(**data)
	current_session.add(event)
	current_session.commit()
	return '', 200


@api.route('/api/user_events', methods=['GET'])
def return_user_events():
	print("starting execution")
	clientid = request.values.get('clientid')
	print("got clientid")
	data = current_session.query(Event).filter(
		Event.clientid == clientid,
	).all()
	print("got data")
	data = [record.as_dict() for record in data]
	print("making dict")
	data = json.dumps(data)
	print("returning data")
	return data, 200
