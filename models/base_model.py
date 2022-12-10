#!/usr/bin/python3
"""This module defines a base class for all models in our hbnb clone"""
import uuid
from datetime import datetime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, DateTime
import models
import os

#Base = declarative_base()

store = 'HBNB_TYPE_STORAGE' 

if store in os.environ.keys() and os.environ['HBNB_TYPE_STORAGE'] == 'db':
    Base = declarative_base()
else:
    Base = object

class BaseModel:
    """A base class for all hbnb models"""
    if store in os.environ.keys() and os.environ['HBNB_TYPE_STORAGE'] == 'db':
        id = Column(
                String(60), unique=True, primary_key=True,
                nullable=False, default=str(uuid.uuid4()))
        created_at = Column(
                DateTime, nullable=False, default=datetime.utcnow())
        updated_at = Column(
                DateTime, nullable=False, default=datetime.utcnow())

    def __init__(self, *args, **kwargs):
        """Instatntiates a new model"""
        s = 'HBNB_TYPE_STORAGE'
        if kwargs:
            self.id = str(uuid.uuid4())
            self.created_at = self.updated_at = datetime.now()
            for k, v in kwargs.items():
                if k == 'created_at' or k == 'updated_at':
                    v = datetime.strptime(v, "%Y-%m-%dT%H:%M:%S.%f")
                if k != "__class__":
                    setattr(self, k, v)
        elif s not in os.environ.keys() or os.environ[
                'HBNB_TYPE_STORAGE'] != 'db':
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)
        else:
            self.id = str(uuid.uuid4())

    def __str__(self):
        """Returns a string representation of the instance"""
        cls = (str(type(self)).split('.')[-1]).split('\'')[0]
        return '[{}] ({}) {}'.format(cls, self.id, self.__dict__)

    def __repr__(self):
        '''returns repr'''
        return self.__str__()

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
