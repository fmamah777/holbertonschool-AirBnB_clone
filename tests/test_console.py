#!/usr/bin/python3
"""Console Unittest"""

import unittest
import pep8
import console
from console import HBNBCommand
from datetime import datetime


class TestConsoleDocs(unittest.TestCase):
    """unittest"""

    def test_module(self):
        """unittest"""
        self.assertIsNot(console.__doc__, None,
                         "console.py needs a docstring")
        self.assertTrue(len(console.__doc__) >= 1,
                        "console.py needs a docstring")

    def test_class(self):
        """unittest"""
        self.assertIsNot(HBNBCommand.__doc__, None,
                         "HBNBCommand class needs a docstring")
        self.assertTrue(len(HBNBCommand.__doc__) >= 1,
                        "HBNBCommand class needs a docstring")

    def test_format(self):
        """unittest"""
        time_format = "%Y-%m-%dT%H:%M:%S.%f"
        hbnb_console = HBNBCommand()
        hbnb_dict = hbnb_console.to_dict()
        self.assertEqual(hbnb_dict["__class__"], "HBNBCommand")
        self.assertEqual(type(hbnb_dict["created_at"]), str)
        self.assertEqual(type(hbnb_dict["updated_at"]), str)
        self.assertEqual(hbnb_dict["created_at"],
                         hbnb_console.created_at.strftime(time_format))
        self.assertEqual(hbnb_dict["updated_at"],
                         hbnb_console.updated_at.strftime(time_format))

    def test_pep8(self):
        """unittest"""
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['models/console.py'])
        self.assertEqual(result.total_errors, 0,
                )
