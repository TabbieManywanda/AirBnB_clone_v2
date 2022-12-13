#!/usr/bin/python3
'''New engine'''


from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm.scoping import scoped_session
from models import *
from models.base_model import Base
import os
from models.base_model import Base


class DBStorage:
    '''New engine'''
    __engine = None
    __session = None
    objects = ["User", "State", "City", "Amenity", "Place", "Review"]

    def __init__(self):
        '''Create engine'''
        self.__engine = create_engine(
                'mysql+mysqldb://' + os.getenv('HBNB_MYSQL_USER') +
                ':' + os.getenv('HBNB_MYSQL_PWD') +
                '@' + os.getenv('HBNB_MYSQL_HOST') +
                ':3306/' +
                os.getenv('HBNB_MYSQL_DB'),
                pool_pre_ping=True)

        try:
            if os.getenv('HBNB_ENV') == "test":
                Base.metadata.drop_all(self.__engine)
        except KeyError:
            pass

    def all(self, cls=None):
        '''Query on current database session'''
        storage = {}
        if cls is None:
            for x in self.objects:
                for instance in self.__session.query(eval(x)):
                    storage[instance.id] = instance
        else:
            if cls not in self.objects:
                return
            for instance in self.__session.query(eval(cls)):
                storage[instance.id] = instance
        return storage

    def new(self, obj):
        '''add the object to the current database session'''
        self.__session.add(obj)

    def save(self):
        '''commit all changes of the current database session'''
        try:
            self.__session.commit()
        except Exception:
            self.__session.rollback()
            raise
        finally:
            self.__session.close()

    def delete(self, obj=None):
        '''delete from the current database session'''
        if obj is None:
            return
        self.__session.delete(obj)

    def reload(self):
        '''create all tables in the database'''
        Base.metadata.create_all(self.__engine)
        self.__session = scoped_session(
                sessionmaker(bind=self.__engine, expire_on_commit=False))

    def close(self):
        '''close session'''
        self.__session.close()
