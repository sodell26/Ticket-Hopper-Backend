from peewee import *

import datetime

from flask_login import UserMixin

DATABASE = SqliteDatabase('tickets.sqlite') # change to 

class TeamMember(UserMixin, Model):
	username = CharField(unique=True)
	email = CharField(unique=True)
	password = CharField()
	#Teams: have the Teams model refer back to this
	#Tickets: same with this one
	Manager = BooleanField(default=False) 

	class Meta:
		database = DATABASE


class Ticket(Model):
	assigned_to = CharField(null=True) # change to a Foreign key after testing
	description = CharField()
	submitted_by = ForeignKeyField(TeamMember, backref = 'my_tickets') # change to a Foreign key after testing
	notes = CharField()
	open_ticket = BooleanField(default=True)
	created = DateTimeField(default=datetime.datetime.now)

	class Meta:
		database = DATABASE

class Team(Model):
	members: ForeignKeyField(TeamMember)
	name: CharField(unique=True)
	active_tickets: ForeignKeyField(Ticket)

#stretch - outside customers
# class Customer(userMixin, Model):
# 	username=CharField(unique=True)
# 	email=CharField(unique=True)
# 	password=CharField()
# 	tickets=ForeignKeyField(Ticket, backref=)



def initialize():
	DATABASE.connect()

	DATABASE.create_tables([TeamMember, Ticket], safe=True)
	print("Connected to DB and created tables if needed")

	DATABASE.close()