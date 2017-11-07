import RPi.GPIO as GPIO
import time
from datetime import datetime
import requests
import json
from flask import Flask




#GPIO.cleanup()
GPIO.setmode(GPIO.BCM)

class Sensor:
	"""A user is sitting on any chair. 
	Users have the following properties:

		Attributes: 
			sitting_distance: A integer representing the user's 
							  distance from the ultrasonic sensor.
			TRIG:             TRIG Pin associated with the Raspberry pi for input
			ECHO:             ECho Pin associated with the Raspberry pi for output
		"""

	def __init__(self, TRIG=18, ECHO=23, sitting_distance=0.0):
		self.TRIG = TRIG
		self.ECHO = ECHO
		self.sitting_distance = sitting_distance
		GPIO.setwarnings(False)
		GPIO.setup(self.TRIG, GPIO.OUT)
		GPIO.setup(self.ECHO, GPIO.IN)


	def read(self):
		GPIO.output(self.TRIG, False)
		GPIO.output(self.TRIG, True)
		time.sleep(0.00001)
		GPIO.output(self.TRIG, False)
		pulse_start, pulse_end = None, None
		while GPIO.input(self.ECHO) == 0:
			pulse_start = time.time()

		while (GPIO.input(self.ECHO) == 1):
			pulse_end = time.time()

		if (pulse_start and pulse_end):
			pulse_duration = pulse_end - pulse_start
			distance = pulse_duration * 17150
			distance = round(distance, 2)
			return int(distance)


def request_to_server(sitting_distance,sitting):
	url="http://192.168.225.122:5000/api/record_event"
	data={'eventtype':'event',
		  'event':sitting,
		  'deviceid':'PT1',
		  'timestamp': str(datetime.now())}
	requests.post(url, data=json.dumps(data))


def client(sitting_distance,sitting):
	# sending requests to server
	print('Client is sitting @ ', str(sitting_distance))
	request_to_server(str(sitting_distance),sitting)


app = Flask(__name__)

sensor = Sensor()
flag = 0
while (True):
	flag = 0
	distance = sensor.read()
	if (distance < 15 and flag == 0):
		flag = 1
		sitting='sit occupied'
		client(str(distance),sitting)
	elif (flag == 1 and distance > 15):
		flag = 0
		sitting='sit unoccupied'
		client(str(distance),sitting)
		
"""
sensor = Sensor()
flag = 0
while (True):
	distance = sensor.read()
	if (distance <  and flag == 0):
		flag = 1
		sitting='sit occupied'
		client(str(distance),sitting)
		time.sleep(10)
	elif (flag == 1 and distance > 15):
		flag = 0
		sitting='sit unoccupied'
		client(str(distance),sitting)
		time.sleep(10)
	
"""
"""
@app.route('/',methods=['GET'])
def get():
	return render_template('index.html')



@app.route('/get_endpoint_distance',methods=['GET'])
def get_endpoint_distance():
	distance=sensor.read()
	return distance
"""