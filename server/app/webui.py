from flask import Blueprint, render_template


webui = Blueprint('webui', __name__)


@webui.route('/', methods=['GET'])
def return_homepage():
	return render_template('homepage.j2')