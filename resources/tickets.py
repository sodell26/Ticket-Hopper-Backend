import models

from flask import Blueprint, request, jsonify

from playhouse.shortcuts import model_to_dict

from flask_login import current_user, login_required

tickets = Blueprint('tickets', 'tickets')

#index, GET route
@tickets.route('/', methods=['GET'])

def tickets_index():
	result = models.Ticket.select()
	print(result)

	ticket_dicts = []
	for ticket in result:
		ticket_dict = model_to_dict(ticket)
		ticket_dicts.append(ticket_dict)

	return jsonify({
		'data': ticket_dicts,
		'message': f"Successfully found {len(ticket_dicts)} tickets",
		'status': 200
		}), 200


#create,POST route
@tickets.route('/', methods=['POST'])
#@login_required

def create_ticket():
	payload = request.get_json()

	new_ticket = models.Ticket.create(assignedto=payload['AssignedTo'], description=payload['Description'], notes=payload['Notes'])
	print(new_ticket)

	ticket_dict = model_to_dict(new_ticket)

	return jsonify(
		data=ticket_dict,
		message='Successfully created new ticket',
		status=201
		), 201