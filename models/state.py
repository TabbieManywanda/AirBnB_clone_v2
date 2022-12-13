#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from models import *
from sqlalchemy import Column, Integer, String
import models
from sqlalchemy.orm import relationship, backref
import os


class State(BaseModel, Base):
    """ State class """
    __tablename__ = 'states'
    name = Column(String(128), nullable=False)
    cities = relationship("City", backref="states", cascade='delete')

    if os.getenv('HBNB_TYPE_STORAGE') != 'db':
        @property
        def cities(self):
            '''list of all related city objects'''
            all_cities = models.storage.all("City")
            tmp = []
            for x in all_cities.values():
                if x.state_id == self.id:
                    tmp.append(x)
            return tmp
