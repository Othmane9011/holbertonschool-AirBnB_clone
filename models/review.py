#!/usr/bin/python3
"""This is review class that inherits from BaseModel."""
from models.base_model import BaseModel


class Review(BaseModel):
    """ Review subclass that inherits from BaseModel """
    place_id = ""
    user_id = ""
    text = ""