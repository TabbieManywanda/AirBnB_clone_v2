#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from models import *
from sqlalchemy import Column, Integer, String
import models
from sqlalchemy.orm import relationship, backref
from os import getenv

store = 'HBNB_TYPE_STORAGE'
if store in os.environ.keys() and os.environ['HBNB_TYPE_STORAGE'] == 'db':
    class State(BaseModel, Base):
        """ State class """

        __tablename__ = 'states'
        name = Column(String(128), nullable=False)
        cities = relationship("City", backref="state")

        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
else:
    class State(BaseModel):
        name=""
        @property
        def cities(self):
            all_cities = models.storage.all("City")
            tmp = []
            for x in all_cities:
                if all_cities[x].state_id == self.id:
                    tmp.append(all_cities[x])
            return tmp
