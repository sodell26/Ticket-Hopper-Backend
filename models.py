from peewee import *
import os
from playhouse.db_url import connect
import datetime

from flask_login import UserMixin

DATABASE = connect(os.environ.get('DATABASE_URL') or 'sqlite:///tickets.sqlite')

class Team(Model):
	name = CharField(unique=True)
	

	class Meta:
		database = DATABASE


class TeamMember(UserMixin, Model):
	username = CharField(unique=True)
	email = CharField(unique=True)
	password = CharField()
	Manager = BooleanField(default=False)

	class Meta:
		database = DATABASE


class Ticket(Model):
	assigned_to = ForeignKeyField(TeamMember, backref='member_ticket', null=True) # change to a Foreign key after testing
	description = CharField()
	submitted_by = ForeignKeyField(TeamMember, backref = 'my_tickets')
	notes = CharField()
	open_ticket = BooleanField(default=True)
	created = DateTimeField(default=datetime.datetime.now)
	team = ForeignKeyField(Team, backref = 'team_tickets', null=True)

	class Meta:
		database = DATABASE


class TeamMemberTeam(Model):
	team = ForeignKeyField(Team, backref='all_teams')
	team_member = ForeignKeyField(TeamMember, backref='team_members')

	class Meta:
		database = DATABASE
	

#stretch - outside customers
# class Customer(userMixin, Model):
# 	username=CharField(unique=True)
# 	email=CharField(unique=True)
# 	password=CharField()
# 	tickets=ForeignKeyField(Ticket, backref=)



def initialize():
	DATABASE.connect()

	DATABASE.create_tables([TeamMember, Ticket, Team, TeamMemberTeam], safe=True)
	print("Connected to DB and created tables if needed")

	DATABASE.close()








