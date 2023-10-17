#!/usr/bin/python3
"""Define the Class Amenity"""
from models.base_model import BaseModel


class Amenity(BaseModel):

    name = ""
    def __init__(self, *args, **kwargs):
        """Initialize a new User object.
        Args:
            args: Non-keyword arguments
            kwargs: Keyword arguments for initializing attributes"""
        super().__init__(*args, **kwargs)
