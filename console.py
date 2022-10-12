#!/usr/bin/python3
""" Console Module """

import cmd
from models.base_model import BaseModel
from models import storage
import json
import shlex
import re
import sys
import cmd
from models import storage
from models.base_model import BaseModel
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User


# entry point of the command
class HBNBCommand(cmd.Cmd):
    """
    HBNBCommand Rules:
        -you can assume arguments are always in the right order
        -each arguments are separated by a space
        -a string argument with a space must be between double quote
        -the error management starts from the first argument to the last one
    """

    # a custom prompt: (hbnb)
    prompt = '(hbnb) '

    def emptyline(self):
        """an empty line and ENTER shouldn’t execute anything"""
        pass

    def can_exit(self):
        """support for do_quit and do_EOF"""
        return True

    def do_quit(self, arg):
        """quit command to exit the program"""
        exit()

    def do_EOF(self, arg):
        """exits the command line at the end of file"""
        exit()

    def do_create(self, model_type="None"):
        """creates a new instance of BaseModel, saves it (to the JSON file)
            and prints the id"""
        # check for class name missing
        if model_type == "" or None:
            print("** class name missing **")
        # check for class name doesn’t exist
        elif model_type not in [
            "BaseModel",
            "City",
            "State",
            "User",
            "Review",
            "Place",
            "Amenity"
        ]:
            print("** class doesn't exist **")
        # check for class name and match to class
        else:
            if model_type == "BaseModel":
                new_model = BaseModel()
            elif model_type == "State":
                new_model = State()
            elif model_type == "City":
                new_model = City()
            elif model_type == "User":
                new_model = User()
            elif model_type == "Place":
                new_model = Place()
            elif model_type == "Amenity":
                new_model = Amenity()
            elif model_type == "Review":
                new_model = Review()
            print(new_model.id)
            # new instance, call to the method new(self) on storage
            storage.new(new_model)
            # call save(self) method of storage
            storage.save()

    def do_show(self, model_key=None):
        """prints the string representation of an instance based on
            the class name and id"""
        class_name = None
        model_id = None
        if model_key != "":
            try:
                class_name = model_key.split(" ")[0]
                model_id = model_key.split(" ")[1]
            except IndexError:
                pass
        # check for class name missing
        if class_name is None:
            print("** class name missing **")
        # check for class name doesn’t exist
        elif class_name not in ["BaseModel", "City", "State",
                                "User", "Review", "Place", "Amenity"]:
            print("** class doesn't exist **")
        # check for id missing
        elif model_id is None:
            print("** instance id missing **")
        # prints the string representation of an instance
        else:
            model_key = class_name + "." + model_id
            key_exists = False
            for key in storage.all().keys():
                if key == model_key:
                    print(storage.all().get(key))
                    key_exists = True
                    break
            if key_exists is not True:
                print("** no instance found **")

    def do_destroy(self, model_key=None):
        """deletes an instance based on the class name and id"""
        class_name = None
        model_id = None
        if model_key != "":
            try:
                class_name = model_key.split(" ")[0]
                model_id = model_key.split(" ")[1]
            except IndexError:
                pass
        # check for class name missing
        if class_name is None:
            print("** class name missing **")
        # check for class name doesn’t exist
        elif class_name not in ["BaseModel", "City", "State",
                                "User", "Review", "Place", "Amenity"]:
            print("** class doesn't exist **")
        # check for id missing
        elif model_id is None:
            print("** instance id missing **")
        # check for class name doesn’t exist for the id
        else:
            model_key = class_name + "." + model_id
            delkey = None
            for key in storage.all().keys():
                if key == model_key:
                    delkey = key
                    break
            if delkey is not None:
                storage.all().pop(key)
                storage.save()
                try:
                    storage.reload()
                except FileNotFoundError:
                    pass
            else:
                print("** no instance found **")

    def do_all(self, model_type):
        """prints all string representation of all instances
            based or not on the class name"""
        obj_list = []
        # printed result must be a list of strings
        if model_type == "":
            for obj in storage.all().values():
                obj_list.append(obj.__str__())
            print(obj_list)
        # check for class name doesn’t exist
        elif model_type not in ["BaseModel", "City", "State",
                                "User", "Review", "Place", "Amenity"]:
            print("** class doesn't exist **")
        # printed result must be a list of strings
        else:
            for obj in storage.all().values():
                if obj.__class__.__name__ == model_type:
                    obj_list.append(obj.__str__())
            print(obj_list)

    # usage: update <class name> <id> <attribute name> "<attribute value>"
    # assume the attribute name is valid
    # assume nobody will try to update list of ids or datetime
    # assume id, created_at and updated_at won’t be passed in the update command
    def do_update(self, model_info):
        """updates an instance based on the class name and
            id by adding or updating attribute"""
        model_type = None
        model_id = None
        model_attr = None
        model_val = None
        # only one attribute can be updated at the time
        if model_info != "":
            try:
                model_type = model_info.split(" ")[0]
                model_id = model_info.split(" ")[1]
                model_attr = model_info.split(" ")[2]
                model_val = model_info.split(" ")[3]
                if model_val.startswith('"'):
                    model_val = model_info.split(" ")[3].strip('"')
                    model_val += " " + model_info.split(" ")[4].strip('"')
            except IndexError:
                pass
        # check for class name missing
        if model_type is None:
            print("** class name missing **")
        # check for id missing
        elif model_id is None:
            print("** instance id missing **")
        # check for attribute name missing
        elif model_attr is None:
            print("** attribute name missing **")
        # check for value for the attribute name doesn’t exist
        elif model_val is None:
            print("** value missing **")
        # attribute value must be casted to the attribute type
        else:
            model_key = model_type + "." + model_id
            key_exists = False
            for key in storage.all().keys():
                if key == model_key:
                    obj = storage.all().get(key)
                    setattr(obj, model_attr, model_val)
                    key_exists = True
                    break
            # check for class name doesn’t exist for the id
            if key_exists is not True:
                print("** no instance found **")


# code should not be executed when imported
if __name__ == '__main__':
    HBNBCommand().cmdloop()
