#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel
from sqlalchemy import Column, Integer, String
import models
from sqlalchemy.orm import relationship, backref
from os import getenv

class State(BaseModel, Base):
    """ State class """

    __tablename__ = 'states'
    name = Column(String(128), nullable=False)

    cities = relationship("City", backref="state",
                          cascade="all, delete, delete-orphan")

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    if getenv('HBNB_TYPE_STORAGE', '') != 'db':
        @property
        def cities(self):
            all_cities = models.storage.all("City")
            tmp = []
            for x in all_cities:
                if all_cities[x].state_id == self.id:
                    tmp.append(all_cities[x])
            return tmp
