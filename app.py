from flask import Flask, jsonify

from resources.tickets import tickets
from resources.users import users
from resources.teams import teams

import models

from flask_cors import CORS 

from flask_login import LoginManager

import os

from dotenv import load_dotenv
load_dotenv()



DEBUG = True
PORT = os.environ.get("PORT_FLASK")

app = Flask(__name__)

app.secret_key = os.environ.get("FLASK_SECRET_KEY")

login_manager = LoginManager()

login_manager.init_app(app)

@login_manager.user_loader
def load_user(user_id):
	return models.TeamMember.get(models.TeamMember.id == user_id)

#CORS
CORS(tickets, origins=['http://localhost:3000'], supports_credentials=True)
CORS(users, origins=['http://localhost:3000'], supports_credentials=True)
CORS(teams, origins=['http://localhost:3000'], supports_credentials=True)


app.register_blueprint(tickets, url_prefix='/api/v1/tickets')
app.register_blueprint(users, url_prefix='/api/v1/users')
app.register_blueprint(teams, url_prefix='/api/v1/teams')

#testing 
# @app.route('/')
# def index():
# 	return 'hi'

if __name__ == '__main__':
	models.initialize()
	app.run(debug=DEBUG, port=PORT)



