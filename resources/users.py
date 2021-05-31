import models

from flask import Blueprint, request, jsonify

from flask_bcrypt import generate_password_hash, check_password_hash

from playhouse.shortcuts import model_to_dict

from flask_login import login_user, logout_user

users = Blueprint('users', 'users')

# @users.route('/', methods=['GET'])
# def testing_user():
# 	return "user route works"


#REGISTER
@users.route('/register', methods=['POST'])
def register():

	payload = request.get_json()

	payload['username'] = payload['username'].lower()

	payload['email'] = payload['email'].lower()

	try:

		models.TeamMember.get(models.TeamMember.email == payload['email'])
		
		# models.TeamMember.get(models.TeamMember.email == payload['email'])

		return jsonify(
			data = {},
			message = f"A user with that email or username already exists",
			status = 401
		), 401

	except models.DoesNotExist:
		#scramble password
		pwd_hash = generate_password_hash(payload['password'])

		#create user
		created_user = models.TeamMember.create(
			username = payload['username'],
			email = payload['email'],
			password = pwd_hash
		)

		login_user(created_user)

		created_user_dict = model_to_dict(created_user)

		created_user_dict.pop('password')

		return jsonify(
			data = created_user_dict,
			message = "Successfully created user",
			status = 201
		), 201


#LOGIN
@users.route('/login', methods=['POST'])
def login():

	payload = request.get_json()
	payload['username'] = payload['username'].lower()
	# payload['email'] = payload['email'].lower()

	try:
		user = models.TeamMember.get(models.TeamMember.username == payload['username'])


		user_dict = model_to_dict(user)

		if (user_dict['username'] == payload['username']):

			password_matches = check_password_hash(user_dict['password'], payload['password'])

			if (password_matches):
				login_user(user)

				user_dict.pop('password')

				return jsonify(
					data = user_dict,
					message = f"Successfully logged in",
					status = 200
				), 200 

			else:
				print('Password doesn\'t match')

				return jsonify(
					data = {},
					message = "password or username doesn't match",
					status = 401
				), 401

		else:
			print('username does not match records')

			return jsonify(
				data = {},
				message = "Username does not match any profiles",
				status = 401
			), 401

	except models.DoesNotExist:
		print('username does not exist')

		return jsonify(
			data = {}, 
			message = "username or password is incorrect",
			status = 401
		), 401


#LOGOUT
@users.route('/logout', methods=['GET'])
def logout():
	logout_user()

	return jsonify (
		data = {},
		status = 200,
		message = 'user has been logged out'
	), 200

	






















































