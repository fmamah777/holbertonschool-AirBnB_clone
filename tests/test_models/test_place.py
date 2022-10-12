#!/usr/bin/python3
"""module for tests on Place class"""

import unittest
from datetime import datetime
import time
from models.place import Place
import re
import json
from models.engine.file_storage import FileStorage
import os
from models import storage
from models.base_model import BaseModel
import uuid


class TestPlace(unittest.TestCase):

    """class containing tests for Place class"""

    def test_attrs(self):
        """unittest"""
        place1 = Place()
        self.assertEqual(place1.name, "")
        self.assertEqual(place1.name, "")
        self.assertEqual(place1.city_id, "")
        self.assertEqual(place1.city_id, "")
        self.assertEqual(place1.user_id, "")
        self.assertEqual(place1.user_id, "")
        self.assertEqual(place1.description, "")
        self.assertEqual(place1.description, "")
        self.assertEqual(place1.number_rooms, 0)
        self.assertEqual(place1.number_rooms, 0)
        self.assertEqual(place1.number_bathrooms, 0)
        self.assertEqual(place1.number_bathrooms, 0)
        self.assertEqual(place1.max_guest, 0)
        self.assertEqual(place1.max_guest, 0)
        self.assertEqual(place1.price_by_night, 0)
        self.assertEqual(place1.price_by_night, 0)
        self.assertEqual(place1.latitude, 0.0)
        self.assertEqual(place1.latitude, 0.0)
        self.assertEqual(place1.longitude, 0.0)
        self.assertEqual(place1.longitude, 0.0)
        self.assertEqual(place1.amenity_ids, [])
        self.assertEqual(place1.amenity_ids, [])
        self.assertIn("id", place1.__dict__)
        self.assertIn("created_at", place1.to_dict())
        self.assertIn("updated_at", place1.to_dict())

    def test_set(self):
        """unittest"""
        place2 = Place()
        place2.name = "Holberton School"
        place2.city_id = "1234"
        place2.user_id = "Holberton-School"
        place2.description = "House of Betty"
        place2.number_rooms = 5
        place2.number_bathrooms = 5
        place2.max_guest = 5
        place2.price_by_night = 918
        place2.latitude = 36
        place2.longitude = 95
        place2.amenity_ids = [
            "free wifi", "projectors",
            "meeting rooms",
            "holbie store", "security"
        ]
        self.assertEqual(place2.name, "Holberton School")
        self.assertEqual(Place.name, "")
        self.assertEqual(place2.city_id, "1234")
        self.assertEqual(Place.city_id, "")
        self.assertEqual(place2.user_id, "Holberton-School")
        self.assertEqual(Place.user_id, "")
        self.assertEqual(place2.description, "House of Betty")
        self.assertEqual(Place.description, "")
        self.assertEqual(place2.number_rooms, 5)
        self.assertEqual(Place.number_rooms, 0)
        self.assertEqual(place2.number_bathrooms, 5)
        self.assertEqual(Place.number_bathrooms, 0)
        self.assertEqual(place2.max_guest, 5)
        self.assertEqual(Place.max_guest, 0)
        self.assertEqual(place2.price_by_night, 918)
        self.assertEqual(Place.price_by_night, 0)
        self.assertEqual(place2.latitude, 36)
        self.assertEqual(Place.latitude, 0.0)
        self.assertEqual(place2.longitude, 95)
        self.assertEqual(Place.longitude, 0.0)
        self.assertEqual(place2.amenity_ids, [
            "free wifi", "projectors",
            "meeting rooms",
            "holbie store", "security"
        ])
        self.assertEqual(Place.amenity_ids, [])

    def test_inheritance(self):
        """unittest"""
        place3 = Place()
        self.assertIsInstance(place3, BaseModel)
        self.assertIsInstance(place3, Place)

    def test_format(self):
        """unittest"""
        time_format = "%Y-%m-%dT%H:%M:%S.%f"
        place4 = Place()
        hbnb_dict = place4.to_dict()
        self.assertEqual(hbnb_dict["__class__"], "Place")
        self.assertEqual(type(hbnb_dict["created_at"]), str)
        self.assertEqual(type(hbnb_dict["updated_at"]), str)
        self.assertEqual(hbnb_dict["created_at"],
                         place4.created_at.strftime(time_format))
        self.assertEqual(hbnb_dict["updated_at"],
                         place4.updated_at.strftime(time_format))

    def test_pep8(self):
        """unittest"""
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['models/place.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")
