#!/usr/bin/python3
"""
The review  module
"""

from models.base_model import BaseModel


class Review(BaseModel):
	"""
	The Review class

	Attributes:
		place_id (str): the place id
		user_id (str): the user id
		text (str): the review content
	"""
	place_id = ""
	user_id = ""
	text = ""


