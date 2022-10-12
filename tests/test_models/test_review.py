#!/usr/bin/python3
"""module for testing review class"""

import unittest
from datetime import datetime
import time
from models.review import Review
import re
import json
from models.engine.file_storage import FileStorage
import os
from models import storage
from models.base_model import BaseModel
import uuid


class TestReview(unittest.TestCase):

    """ tests for review"""

    def test_attrs(self):
        """unittest"""
        review1 = Review()
        self.assertEqual(review1.place_id, "")
        self.assertEqual(Review.place_id, "")
        self.assertEqual(review1.user_id, "")
        self.assertEqual(Review.user_id, "")
        self.assertEqual(review1.text, "")
        self.assertEqual(Review.text, "")
        self.assertIn("id", review1.__dict__)
        self.assertIn("created_at", review1.to_dict())
        self.assertIn("updated_at", review1.to_dict())

    def test_set(self):
        """unittest"""
        review2 = Review()
        review2.place_id = "5678"
        review2.user_id = "Holberton-School"
        review2.text = "two thumbs up"
        self.assertEqual(review2.place_id, "5678")
        self.assertEqual(Review.place_id, "")
        self.assertEqual(review2.user_id, "Holberton-School")
        self.assertEqual(Review.user_id, "")
        self.assertEqual(review2.text, "two thumbs up")
        self.assertEqual(Review.text, "")

    def test_inheritance(self):
        """unittest"""
        review3 = Review()
        self.assertIsInstance(review3, BaseModel)
        self.assertIsInstance(review3, Review)

    def test_format(self):
        """unittest"""
        time_format = "%Y-%m-%dT%H:%M:%S.%f"
        review4 = Review()
        hbnb_dict = review4.to_dict()
        self.assertEqual(hbnb_dict["__class__"], "Review")
        self.assertEqual(type(hbnb_dict["created_at"]), str)
        self.assertEqual(type(hbnb_dict["updated_at"]), str)
        self.assertEqual(hbnb_dict["created_at"],
                         review4.created_at.strftime(time_format))
        self.assertEqual(hbnb_dict["updated_at"],
                         review4.updated_at.strftime(time_format))

    def test_pep8(self):
        """unittest"""
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['models/review.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")
