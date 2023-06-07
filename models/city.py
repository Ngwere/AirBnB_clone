#!/usr/bin/python3
"""
The city module
"""

from models.base_model import BaseModel


class City(BaseModel):
	"""
	The City class

	Attributes:
		name(str): the name of the state
		state_id(str): the state id
	"""
	name = ""
	state_id = ""


