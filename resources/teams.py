import models

from flask import Blueprint, request, jsonify

from playhouse.shortcuts import model_to_dict

from flask_login import current_user, login_required

teams = Blueprint('teams', 'teams')

#index, GET route
@teams.route('/', methods=['GET'])

def team_index():
	result = models.Team.select()


	team_dicts = [model_to_dict(team) for team in result]

	return jsonify({
		'data': team_dicts,
		'message': f"Successfully found {len(team_dicts)} teams",
		'status': 200
		}), 200


#create,POST route
@teams.route('/', methods=['POST'])
#@login_required

def create_team():
	payload = request.get_json()

	new_team = models.Team.create(description=payload['description'], notes=payload['notes'], submitted_by = current_user.id)
	print(new_team)

	team_dict = model_to_dict(new_team)

	return jsonify(
		data=team_dict,
		message='Successfully created new team',
		status=201
		), 201



#update/PUT route
@teams.route('/<id>', methods=['PUT'])
def edit_one_team(id):
	payload = request.get_json()
	models.Team.update(**payload).where(models.Team.id == id).execute()
	return jsonify(
		data=model_to_dict(models.Team.get_by_id(id)),
		message="Successfully updated team",
		status=200
		),200


#show/GET route
@teams.route('/<id>', methods=['GET'])
def show_one_team(id):
	team = models.Team.get_by_id(id)

	return jsonify(
		data = model_to_dict(team),
		message = "showing one team",
		status = 200
	), 200


#delete route
@teams.route('/<id>', methods=['DELETE'])
def delete_team(id):

	models.Team.delete().where(models.Team.id==id).execute()

	return jsonify(
		data = None,
		message='team deleted',
		status=200
	), 200




	




































