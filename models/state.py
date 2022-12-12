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
    if models.store == "db":
        cities = relationship("City", backref="state", cascade='all, delete')

    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    else:
        @property
        def cities(self):
            all_cities = models.storage.all("City")
            tmp = []
            for x in all_cities:
                if all_cities[x].state_id == self.id:
                    tmp.append(all_cities[x])
            return tmp
