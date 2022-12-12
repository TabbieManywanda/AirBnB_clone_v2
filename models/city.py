#!/usr/bin/python3
""" City Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import relationship
import os
from uuid import uuid4


store = 'HBNB_TYPE_STORAGE'
class City(BaseModel, Base):
    """ The city class, contains state ID and name """
    if store in os.environ.keys() and os.environ['HBNB_TYPE_STORAGE'] == 'db':
        __tablename__ = 'cities'
        state_id = Column(String(60), ForeignKey('states.id'), nullable=False)
        name = Column(String(128), nullable=False)
        places = relationship('Place', backref='cities', cascade='all, delete')

    else:
        """city class"""
        state_id = ''
        name = ''

    def __init__(self, **kwargs):
        '''Init'''
        setattr(self, 'id', str(uuid4()))
        for x, y in kwargs.items():
            setattr(self, x, y)