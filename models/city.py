#!/usr/bin/python3
from models.base_model import BaseModel
"""Defines the class City"""


class City(BaseModel):
    state_id = ""
    name = ""
     def __init__(self, *args, **kwargs):
         """Initialize a new User object.
        Args:
            args: Non-keyword arguments
            kwargs: Keyword arguments for initializing attributes"""

            super().__init__(*args, **kwargs)
