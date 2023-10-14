#!/usr/bin/python3
"""Defines The Class Review """
from models.base_model import BaseModel


class Review(BaseModel):

    place_id = ""
    user_id = ""
    text = ""

    def __init__(self, *args, **kwargs):
        """Initialize a new User object.
        Args:
            args: Non-keyword arguments
            kwargs: Keyword arguments for initializing attributes"""
        super().__init__(*args, **kwargs)
