import models

from flask import Blueprint, request, jsonify

from playhouse.shortcuts import model_to_dict

from flask_login import current_user, login_required

tickets = Blueprint('tickets', 'tickets')

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

