from flask import Flask, request


app = Flask(__name__)


@app.route('/api/record_event', methods=['POST'])
def record_event():
	print(request.data)
	return '', 200


if __name__ == '__main__':
	app.run()
