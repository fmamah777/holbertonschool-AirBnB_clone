#!/usr/bin/python3
"""FileStorage Unittest"""

import unittest
import pep8
import json
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
from datetime import datetime


class TestFileStorage(unittest.TestCase):
    """unittest"""

    storage = None
    base_model1 = None
    base_model = None

    @classmethod
    def setUpClass(cls):
        """unittest"""
        cls.base_model = BaseModel()
        cls.base_model1 = BaseModel()
        cls.storage = FileStorage()

    @classmethod
    def tearDownClass(cls):
        """unittest"""
        del cls.base_model
        del cls.base_model1
        del cls.storage

    def test_all(self):
        """unittest"""
        objects = self.storage.all()
        self.assertIsInstance(objects, dict)
        key = "{}.{}".format(type(self.base_model).__name__, self.base_model.id)
        self.assertIn(key, objects)
        self.assertEqual(self.base_model, objects.get(key))
        key1 = "{}.{}".format(type(self.base_model1).__name__, self.base_model1.id)
        self.assertIn(key1, objects)
        self.assertEqual(self.base_model1, objects.get(key1))

    def test_new(self):
        """unittest"""
        attr_dict = {"attribute": "value"}
        new_obj = BaseModel(**attr_dict)
        objects = self.storage.all()
        key_new = "{}.{}".format(type(new_obj).__name__, new_obj.id)
        self.assertNotIn(key_new, objects)
        self.storage.new(new_obj)
        self.assertIn(key_new, objects)
        key = "{}.{}".format(type(self.base_model).__name__, self.base_model.id)
        self.assertIn(key_new, objects)
        self.assertEqual(self.base_model, objects.get(key))

    def test_save(self):
        """unittest"""
        objects = self.storage.all()
        self.storage.save()
        with open("file.json", 'r') as f:
            from_file = f.read()
        self.assertEqual(from_file, json.dumps({
            key: value.to_dict()
            for key, value in
            objects.items()
        }))

    def test_reload(self):
        """unittest"""
        before = self.storage.all()
        self.storage.reload()
        after = self.storage.all()
        self.assertDictEqual(before, after)

    def test_format(self):
        """unittest"""
        time_format = "%Y-%m-%dT%H:%M:%S.%f"
        file_storage = FileStorage()
        hbnb_dict = file_storage.to_dict()
        self.assertEqual(hbnb_dict["__class__"], "FileStorage")
        self.assertEqual(type(hbnb_dict["created_at"]), str)
        self.assertEqual(type(hbnb_dict["updated_at"]), str)
        self.assertEqual(hbnb_dict["created_at"], file_storage.created_at.strftime(time_format))
        self.assertEqual(hbnb_dict["updated_at"], file_storage.updated_at.strftime(time_format))

    def test_pep8(self):
        """unittest"""
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['models/engine/file_storage.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")
