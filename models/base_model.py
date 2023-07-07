#!/usr/bin/python3
""" BaseMode1 """
import uuid
import models
from datetime import datetime
from models import storage


class BaseModel():
    """ Defines all common attributes/methods for other classes """
    def __init__(self, *args, **kwargs):
        """ kwargs: keyarguments used to give multiple arguments """
        if kwargs:
            date_format = "%Y-%m-%dT%H:%M:%S.%f"
            k_dict = kwargs.copy()
            del k_dict["__class__"]
            for key in k_dict:
                if (key == "created_at" or key == "updated_at"):
                    k_dict[key] = datetime.strptime(k_dict[key], date_format)
            self.__dict__ = k_dict
        else:
            """ uuid.uuid4() is used to generate a unique id """
            self.id = str(uuid.uuid4())
            self.created_at = datetime.today()
            self.updated_at = datetime.today()
            storage.new(self)

    def save(self):
        """ Updates update_at """
        self.updated_at = datetime.today()
        storage.save()

    def __str__(self):
        """Return the print/str representation of the BaseModel instance."""
        clname = self.__class__.__name__
        return "[{}] ({}) {}".format(clname, self.id, self.__dict__)

    def to_dict(self):
        """Return a dictionary representation of the BaseModel instance."""
        new_dict = self.__dict__.copy()
        new_dict["__class__"] = self.__class__.__name__
        new_dict["created_at"] = self.created_at.isoformat()
        new_dict["updated_at"] = self.updated_at.isoformat()
        return new_dict