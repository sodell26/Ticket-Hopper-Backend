import models

from flask import Blueprint, request, jsonify

from playhouse.shortcuts import model_to_dict

from flask_login import current_user, login_required

tickets = Blueprint('tickets', 'tickets')

#index, GET route
@tickets.route('/', methods=['GET'])

def tickets_index():
	result = models.Ticket.select()
	# print(result)

	for ticket in result:
		print(ticket.__data__)

	# ticket_dicts = [model_to_dict(ticket) for ticket in current_user.my_tickets]
	ticket_dicts = [model_to_dict(ticket) for ticket in result]

	# print(ticket_dicts)
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

	new_ticket = models.Ticket.create(description=payload['description'], notes=payload['notes'], submitted_by = current_user.id)
	print(new_ticket)

	ticket_dict = model_to_dict(new_ticket)

	return jsonify(
		data=ticket_dict,
		message='Successfully created new ticket',
		status=201
		), 201



#update/PUT route
@tickets.route('/<id>', methods=['PUT'])
def edit_one_ticket(id):
	payload = request.get_json()
	models.Ticket.update(**payload).where(models.Ticket.id == id).execute()
	return jsonify(
		data=model_to_dict(models.Ticket.get_by_id(id)),
		message="Successfully updated ticket",
		status=200
		),200


#show/GET route
@tickets.route('/<id>', methods=['GET'])
def show_one_ticket(id):
	ticket = models.Ticket.get_by_id(id)

	return jsonify(
		data = model_to_dict(ticket),
		message = "showing one ticket",
		status = 200
	), 200


#delete route
@tickets.route('/<id>', methods=['DELETE'])
def delete_ticket(id):

	models.Ticket.delete().where(models.Ticket.id==id).execute()

	return jsonify(
		data = None,
		message='ticket deleted',
		status=200
	), 200




	




































