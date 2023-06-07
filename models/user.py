#!/usr/bin/python3
"""
The user module
"""

from models.base_model import BaseModel


class User(BaseModel):
	"""
	The user class

	Attributes:
		email(str): the user email
		password(str): the user password
		firs_name: the user firs name 
		last_name(str): the user lase name
	"""
	email = ""
	password = ""
	first_name = ""
	last_name = ""


