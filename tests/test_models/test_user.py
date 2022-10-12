#!/usr/bin/python3
"""module for testing user class n stuff"""

import unittest
from datetime import datetime
import time
from models.user import User
import re
import json
from models.engine.file_storage import FileStorage
import os
from models import storage
from models.base_model import BaseModel
import uuid


class TestUser(unittest.TestCase):

    """class containing testssss"""
class TestUser(unittest.TestCase):

    def test_attrs(self):
        """unitest"""
        user1 = User()
        self.assertEqual(user1.email, "")
        self.assertEqual(user1.first_name, "")
        self.assertEqual(user1.last_name, "")
        self.assertEqual(user1.password, "")
        self.assertIn("id", user1.__dict__)
        self.assertIn("created_at", user1.__dict__)
        self.assertIn("updated_at", user1.__dict__)
        self.assertEqual(User.email, "")
        self.assertEqual(User.password, "")
        self.assertEqual(User.first_name, "")
        self.assertEqual(User.last_name, "")

    def test_set(self):
        """unittest"""
        user2 = User()
        user2.email = "example@holberton.com"
        self.assertEqual(user2.email, "example@holberton.com")
        user2.password = "holberton123"
        self.assertEqual(user2.password, "holberton123")
        user2.first_name = "Betty"
        self.assertEqual(user2.first_name, "Betty")
        user2.last_name = "Holberton"
        self.assertEqual(user2.last_name, "Holberton")

    def test_inheritance(self):
        """unittest"""
        user3 = User()
        self.assertIsInstance(user3, BaseModel)
        self.assertIsInstance(user3, User)

    def test_dict(self):
        """unittest"""
        user4 = User()
        dict_test = user4.to_dict()
        self.assertIn("__class__", dict_test)
        self.assertIn("created_at", dict_test)
        self.assertIn("updated_at", dict_test)

    def test_format(self):
        """unittest"""
        time_format = "%Y-%m-%dT%H:%M:%S.%f"
        user5 = User()
        hbnb_dict = user5.to_dict()
        self.assertEqual(hbnb_dict["__class__"], "User")
        self.assertEqual(type(hbnb_dict["created_at"]), str)
        self.assertEqual(type(hbnb_dict["updated_at"]), str)
        self.assertEqual(hbnb_dict["created_at"],
                         user5.created_at.strftime(time_format))
        self.assertEqual(hbnb_dict["updated_at"],
                         user5.updated_at.strftime(time_format))

    def test_pep8(self):
        """unittest"""
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['models/user.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")
