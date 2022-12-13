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
        if cls is None:
            return FileStorage.__objects
        storage = {}
        for x in FileStorage.__objects:
            object_cls = FileStorage.__objects[x].__class__.__name__
            if cls == object_cls:
                storage[x] = FileStorage.__objects[x]
        return storage

    def new(self, obj):
        """Adds new object to storage dictionary"""
        if obj is not None:
            FileStorage.__objects[obj.id] = obj

    def save(self):
        """Saves storage dictionary to file"""
        store = {}
        for key in FileStorage.__objects.keys():
            store[key] = FileStorage.__objects[key].to_json()
        with open(FileStorage.__file_path, 'w') as f:
            f.write(json.dumps(store))

    def update(self, cls, obj_id, key, new_value):
        '''updates'''
        if obj_id not in FileStorage.__objects:
            return 0
        obj = FileStorage.__objects[obj_id]
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
        FileStorage.__objects.pop(obj.id, 0)

    def close(self):
        '''close'''
        self.save()
