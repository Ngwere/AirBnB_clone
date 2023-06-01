#!/usr/bin/python3
"""
The BaseModel package
"""

import uuid
import datetime

class BaseModel:
    """Custom base for alll the classes in the AirBnB consol project 

    Arguments:
        id(str): handles unique user identity
        created_at: assigns current datetime
        updated_at: updates current datetime
    Methods:
        __str__: prints te class name, id, and creates dictionary representation of the model input values
        save(self): updates instance attributes with current dictionary datetime
        to_dict(self): returns the dictionary of the model attributes
    """
    def __init__(self, *args, **kwargs):
        """Initialize BaseModel instance"""
        self.id = str(uuid.uuid4())
        self.created_at = datetime.datetime.now()
        self.updated_at = self.created_at

    def __str__(self):
        """Return string representation of BaseModel instance"""
        return "[{}] ({}) {}".format(type(self).__name__, self.id, self.__dict__)

    def save(self):
        """Update the public instance attribute updated_at with the current datetime"""
        self.updated_at = datetime.datetime.now()

    def to_dict(self):
        """Return a dictionary containing all keys/values of __dict__ of the instance"""
        dic = self.__dict__.copy()
        dic['__class__'] = type(self).__name__
        dic['created_at'] = self.created_at.isoformat()
        dic['updated_at'] = self.updated_at.isoformat()
        return dic
