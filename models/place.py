#!/usr/bin/python3
"""
The place module
"""

from models.base_model import BaseModel


class Place(BaseModel):
	"""
	The Place class

	Attributes:
		name(str): the name of the place 
		city_id(str): City id
		user_id(str): user id
		description (str): description of the place
		number_rooms (int): the number of rooms of the place
		number_bathrooms (int): the number of bathrooms of the place
		max_guest (int): maximum nuber of guests of the place
		price_by_night (int): price by night of the place
		latitude (float): latitude of thelace
		longitude (float): longitude of the place
		amenity_ids (list): list of amenity ids
	"""
	name = ""
	city_id = ""
	user_id = ""
	description = ""
	number_rooms = 0
	number_bathrooms = 0
	max_guest = 0
	price_by_night = 0
	latitude = 0.0
	longitude = 0.0
	amenity_ids = []
