#!/usr/bin/python3
from models.base_model import BaseModel
""" Defines the Class User """

class User(BaseModel):
    
    email = ""
    password = ""
    first_name = ""
    last_name = ""

    def __init__(self, *args, **kwargs):
    """Initialize a new User object.
            Args:
            args: Non-keyword arguments
            kwargs: Keyword arguments for initializing attributes"""
    
    super().__init__(*args, **kwargs)
