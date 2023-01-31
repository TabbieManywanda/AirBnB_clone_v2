#!/usr/bin/python3
"""This module defines a class to manage file storage for hbnb clone"""
import json
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review


class FileStorage:
    """This class manages storage of hbnb models in JSON format"""
    __file_path = 'file.json'
    __objects = {}

    def __init__(self):
        '''initializing'''
        self.reload()

    def all(self, cls=None):
        """Returns a dictionary of models currently in storage"""
        if cls is not None:
            #return FileStorage.__objects
            storage = {}
            for key, value in self.__objects.items:
                if cls == type(value):
                    storage[key] = value
            return storage
        return self.__objects

    def new(self, obj):
        """Adds new object to storage dictionary"""
        if obj is not None:
            self.__objects[obj.id] = obj

    def save(self):
        """Saves storage dictionary to file"""
        store = {}
        for key in self.__objects.keys():
            store[key] = self.__objects[key].to_json()
        with open(self.__file_path, 'w') as f:
            f.write(json.dumps(store))

    def update(self, cls, obj_id, key, new_value):
        '''updates'''
        if obj_id not in self.__objects:
            return 0
        obj = self.__objects[obj_id]
        setattr(obj, key, new_value)
        return 1

    def reload(self):
        """Loads storage dictionary from file"""
        try:
            with open(self.__file_path, 'r') as f:
                for val in json.load(f).values():
                    name = val['__class__']
                    del val['__class__']
                    self.new(eval(name)(**val))
        except Exception:
            pass

    def delete(self, obj=None):
        """Deletes an object from __objects"""
        if obj is None:
            return
        self.__objects.pop(obj.id, 0)

    def close(self):
        '''calls reload'''
        self.reload()
