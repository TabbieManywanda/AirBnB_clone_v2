#!/usr/bin/python3
"""This module defines a class User"""
import models
from models.base_model import BaseModel, Base
import os
from models import store
import sqlalchemy
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship


store = 'HBNB_TYPE_STORAGE'
if store in os.environ.keys() and os.environ['HBNB_TYPE_STORAGE'] == 'db':
    class User(BaseModel, Base):
        """This class defines a user by various attributes"""
        __tablename__= 'users'
        email = Column(String(128), nullable=False)
        password = Column(String(128), nullable=False)
        first_name = Column(String(128), nullable=True)
        last_name = Column(String(128), nullable=True)
        places = relationship('Place', backref='user')
        reviews = relationship('Review', backref='user')

        def __init__(self, *args, **kwargs):
            """Initializes a user"""
            super().__init__(*args, **kwargs)

else:
    class User(BaseModel):
        email=""
        password=""
        first_name=""
        last_name=""

        