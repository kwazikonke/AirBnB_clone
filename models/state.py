#!/usr/bin/python3
"""Defines the Class State"""
from models.base_model import BaseModel

class State(BaseModel):
       name = ""

       def __init__(self, *args, **kwargs):
"""Initialize a new User object.
        Args:
            args: Non-keyword arguments
            kwargs: Keyword arguments for initializing attributes"""

            super().__init__(*args, **kwargs)
