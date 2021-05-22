from peewee import *

import datetime

from flask_login import UserMixin

DATABASE = SqliteDatabase('tickets.sqlite') # change to 

class Ticket(Model):
	AssignedTo: CharField() # change to a Foreign key after testing
	Description: CharField()
	SubmittedBy: CharField() # change to a Foreign key after testing
	Notes: CharField()
	Open: BooleanField()
	Created: DateTimeField(default=datetime.datetime.now)

	class Meta:
		database = DATABASE


# class Customer(userMixin, Model):
# 	username=CharField(unique=True)
# 	email=CharField(unique=True)
# 	password=CharField()
# 	tickets=ForeignKeyField(Ticket, backref=)








def initialize():
	DATABASE.connect()

	DATABASE.create_tables([Ticket], safe=True)
	print("Connected to DB and created tables if needed")

	DATABASE.close()