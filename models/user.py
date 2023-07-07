#!/usr/bin/python3
""" This is the User class that inherits from BaseModel """
from models.base_model import BaseModel


class User(BaseModel):
    """ User subclass that inherits from BaseModel """
    email = ""
    password = ""
    first_name = ""
    last_name = ""