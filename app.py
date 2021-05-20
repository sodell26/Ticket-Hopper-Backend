from flask import Flask, jsonify

# from resources.tickets import tickets
# from resources.users import users

import models

from flask_cors import CORS 

from flask_login import LoginManager

import os

from dotenv import load_dotenv
load_dotenv()



DEBUG = True
PORT = os.environ.get("PORT_FLASK")

# app.secret_key = os.environ.get("FLASK_SECRET_KEY")

# login_manager = LoginManager()

# login_manager.init_app(app)

# @login_manager.user_loader

app = Flask(__name__)

@app.route('/')
def index():
	return 'hi'






























if __name__ == '__main__':
	app.run(debug=DEBUG, port=PORT)