#!/usr/bin/python3
"""This module defines a base class for all models in our hbnb clone"""
import uuid
from datetime import datetime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, DateTime
import models
import os

Base = declarative_base()

# store = 'HBNB_TYPE_STORAGE'

# if store in os.environ.keys() and os.environ['HBNB_TYPE_STORAGE'] == 'db':
#     Base = declarative_base()
# else:
#     Base = object


class BaseModel:
    """A base class for all hbnb models"""

    id = Column(
            String(60), unique=True, primary_key=True,
            nullable=False, default=str(uuid.uuid4()))
    created_at = Column(
            DateTime, nullable=False, default=datetime.utcnow())
    updated_at = Column(
            DateTime, nullable=False, default=datetime.utcnow())

    def __init__(self, *args, **kwargs):
        """Instatntiates a new model"""
        # s = 'HBNB_TYPE_STORAGE'
        if kwargs:
            if "id" not in kwargs.keys():
                self.id = str(uuid.uuid4())
            if "created_at" not in kwargs.keys():
                self.created_at = datetime.now()
            if "updated_at" not in kwargs.keys():
                self.updated_at = datetime.now()
            for key, value in kwargs.items():
                if key == "created_at" or key == "updated_at":
                    value = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
                if key != '__class__':
                    setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = self.updated_at = datetime.now()

    def __str__(self):
        """Returns a string representation of the instance"""
        cls = (str(type(self)).split('.')[-1]).split('\'')[0]
        return '[{}] ({}) {}'.format(cls, self.id, self.__dict__)

    def save(self):
        """Updates updated_at with current time when instance is changed"""
        self.updated_at = datetime.now()
        models.storage.new(self)
        models.storage.save()

    def to_dict(self):
        """Convert instance into dict format"""
        dictionary = dict(self.__dict__)
        dictionary['__class__'] = str(type(self).__name__)
        dictionary['created_at'] = self.created_at.isoformat()
        dictionary['updated_at'] = self.updated_at.isoformat()
        if '_sa_instance_state' in dictionary.keys():
            del dictionary['_sa_instance_state']
            models.storage.save()
        return dictionary

    def delete(self):
        """delete the current instance from the storage"""
        models.storage.delete(self)
        models.storage.save()
