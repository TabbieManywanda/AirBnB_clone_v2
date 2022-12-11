#!/usr/bin/python3
"""This module instantiates an object of class FileStorage"""
from models.engine.file_storage import FileStorage
from models.engine.db_storage import DBStorage
import os

store = 'HBNB_TYPE_STORAGE'
if store in os.environ.keys() and os.environ['HBNB_TYPE_STORAGE'] == 'db':
    storage = DBStorage()
    storage.reload()
else:
    storage = FileStorage()
storage.reload()
