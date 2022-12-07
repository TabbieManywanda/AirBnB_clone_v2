#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey, Integer, Table, Float
from sqlalchemy.orm import relationship
import os
from uuid import uuid4


place_amenity = Table('place_amenity', Base.metadata,
        Column('place_id', String(60), ForeignKey('places.id'), nullable=False),
        Column('amenity_id', String(60), ForeignKey('amenities.id'), nullable=False))

store = 'HBNB_TYPE_STORAGE'
if store in environ.keys() and environ['HBNB_TYPE_STORAGE'] == 'db':
    class Place(BaseModel, Base):
        """ A place to stay """
        __tablename__ = 'places'
        city_id = Column(String(60), ForeignKey('cities.id'), nullable=False)
        user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
        name = Column(String(128), nullable=False)
        description = Column(String(1024), nullable=True)
        number_rooms = Column(Integer, nullable=False, default=0)
        number_bathrooms = Column(Integer, nullable=False, default=0)
        max_guest = Column(Integer, nullable=False, default=0)
        price_by_night = Column(Integer, nullable=False, default=0)
        latitude = Column(Float, nullable=True)
        longitude = Column(Float, nullable=True)
        reviews = relationship("Review", backref="place")
        amenities = relationship("Amenity",
                                 secondary=place_amenity, viewonly=False)

        def __init__(self, **kwargs):
            setattr(self, 'id', str(uuid4()))
            for x, y in kwargs.items():
                setattr(self, x, y)

else:
    class Place(BaseModel):
        '''class place'''
        city_id = ''
        user_id = ''
        name = ''
        description = ''
        number_rooms = 0
        number_bathrooms = 0
        max_guest = 0
        price_by_night = 0
        latitude = 0.0
        longitude = 0.0
        amenity_ids = []

        @property
        def reviews(self):
            all_review = models.storage.all(Review)
            lists = []
            keys = all_review.items()
            for x, y in keys:
                if 'Review' == x[0:4] and y.place.id == self.id:
                    lists.append(y)
            return(lists)
