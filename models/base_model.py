#!/usr/bin/python3
"""
The BaseModel package
"""
import models
from uuid import uuid4
from datetime import datetime

class BaseModel:
    """Custom base for alll the classes in the AirBnB consol project 

    Attributes:
        id(str): handles unique user identity
        created_at: assigns current datetime
        updated_at: updates current datetime
    Methods:
        __str__: prints te class name, id, and creates dictionary representation of the model input values
        save(self): updates instance attributes with current dictionary datetime
        to_dict(self): returns the dictionary of the model attributes
    """
    def __init__(self, *args, **kwargs):
        """Initialize BaseModel instance

        Args:
            *args(args): arguments
            **kwargs(dict): attributes values

        """
        DATE_TIME_FORMAT = '%Y-%m-%dT%H:%M:%S.%f'
        if not kwargs:
            self.id = str(uuid4())
            self.created_at = datetime.utcnow()
            self.updated_at = datetime.utcnow()
            models.storage.new(self)
        else:
            for key, value in kwargs.items():
                if key in ("update_at", "created_at"):
                    self.__dict__[key] = datetime.strptime(value, DATE_TIME_FORMAT)
                elif key[0] == "id":
                    self.__dict__[key] = str(value)
                else:
                    self.__dict__[key] = value
                   
    def __str__(self):
        """Return string representation of BaseModel instance"""
        return "[{}] ({}) {}".format(type(self).__name__, self.id, self.__dict__)

    def save(self):
        """Update the public instance attribute updated_at with the current datetime"""
        self.updated_at = datetime.utcnow()
        models.storage.save()

    def to_dict(self):
        """
        Method returns a dictionary containing all 
        keys/values of __dict__ instance
        """
        map_objects = {}
        for key, value in self.__dict__.items():
            if key == "created_at" or key == "updated_at":
                map_objects[key] = value.isoformat()
            else:
                map_objects[key] = value
        map_objects["__cet ass__"] = self.__class__.__name__
        return map_objects
