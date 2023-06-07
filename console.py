#!/usr/bin/python3
"""HBNBCommand interpreter
   version: 0.1
"""
import re
import json
import models
import cmd
from models.base_model import BaseModel
from models.user import User 
from models.review import Review
from models.place import Place
from models.state import State
from models.amenity import Amenity
from models.city import City

class HBNBCommand(cmd.Cmd):
	"""
	Custom console class
	"""

	prompt = '(hbnb) '

	def my_errors(self, line, num_of_args):
		"""Displays error messages to use

		Args:
			line(any): gets user input using command line
			num_of_args(int): number of input arguments

		Description:
			Displays output to the use based on
			the input commands.
		"""
		classes = ["BaseModel", "User", "State", "City",
			"Amenity", "Place", "Review"]
	
		msg = ["** class name missing **",
               		"** class doesn't exist **",
               		"** instance id missing **",
               		"** no instance found **",
               		"** attribute name missing **",
               		"** value missing **"]
		if not line:
			print(msg[0])
			return 1
		args = line.split()

		for i in range(len(args)):
			if args[i][0] == '"':
				args[i] = args[i].replace('"', "")
		if num_of_args >= 1 and args[0] not in classes:
			print(msg[1])
			return 1
		elif num_of_args == 1:
			return 0
		if num_of_args >= 2 and len(args) < 2:
			print(msg[2])
			return 1
		d = models.storage.all()

		key = args[0] + '.' + args[1]
		if num_of_args >= 2 and key not in d:
			print(msg[3])
			return 1
		elif num_of_args == 2:
			return 0
		if num_of_args >= 4 and len(args) < 3:
			print(msg[4])
			return 1
		if num_of_args >= 4 and len(args) < 4:
			print(msg[5])
			return 1
		return 0

	def do_quit(self, line):
		"""
		Quit the command interpreter terminal using the quit command

		Args:
			line(arg): input argument for quiting the terminal
		"""
		return True
	
	def do_EOF(self, line):
		""" 
		Quit command interpreter by ctrl + D or end of line

		Arg:
			line(arg): input argument for quiting the terminal
		"""
		return True

	def emptyline(self):
		"""	
		Do nothing when an empty line is pressed.
		"""
		pass

	def do_create(self, line):
		"""
		create  new instance of object and save it in the file storage

		Args:
			line(arg): input argument for creating the object
			usage: $ create myClass
		"""
		if (self.my_errors(line, 1) == 1):
			return
		args = line.split(" ")
		
		obj = eval(args[0])()
		obj.save()

		print(obj.id)

	def do_show(self, line):
		"""       
		Prints the string representation of an instance by class name and id. 
		useage: $ show BaseModel 1234-1234-1234

                Args:
                        line(arg): input argument for creating the object
                        usage: $ create myClass
		"""
		if (self.my_errors(line, 1) == 1):
			return

		if (self.my_errors(line, 2) == 1):
			return
		args = line.split(" ")
		d = models.storage.all()

		if args[1][0] == '"':
			args[1] = args[1].replace('"', "")
		key = args[0] + '.' + args[1]
		print(d[key])

	def do_destroy(self, line):
		"""
		Delete an instance by class name and id.
		useage: $ destroy BaseModel 1234-1234-1234

		Args:
			line(arg): input argument for creating the object
		"""
		if (self.my_errors(line, 1) == 1):
			return
		if (self.my_errors(line, 2) == 1):
			return
		args = line.split(" ")
		d = models.storage.all()

		if args[1][0] == '"':
			args[1] = args[1].replace('"', "")
		key = args[0] + '.' + args[1]
		del d[key]
		models.storage.save()
	
	def do_all(self, line):
		"""
		Print all string instances in file storage
		usage: $ all or $ all BaseModel

		Args:
			line(arg): the arguments for displaying objects
		"""
		d = models.storage.all()
		args = line.split(" ")
		if not line:
			print([str(v) for v in d.values()])
			return
		if (self.my_errors(line, 1) == 1):
			return
		print([str(v) for v in d.values()
			if v.__class__.__name__ == args[0]])
	
	def do_update(self, line):
		"""
		Update class and id by changing attribute
		Usage: update <class name> <id> <attribute name> "<attribute value>"

		Args:
			line(arg): the arguments for updating instance of object
		"""
		if (self.my_errors(line, 1) == 1):
			return
		if (self.my_errors(line, 2) == 1):
			return
		if (self.my_errors(line, 4) == 1):
			return
		args = line.split()
		d = models.storage.all()
		for i in range(len(args[1:]) + 1):
			if args[i][0] =='"':
				args[i] = args[i].replace('"',"")
		key = args[0] + '.' + args[1]
		attr_k = args[2]
		attr_v = args[3]
		try:
			if attr_v.isdigit():
				attr_v = int(attr_v)
			elif float(attr_v):
				attr_v = float(attr_v)
		except ValueError:
			pass
		class_attr = type(d[key]).__dict__
		if attr_k in class_attr.keys():
			try:
				attr_v = type(class_attr[attr_k])(attr_v)
			except Exception:
				print("** You've entered wrong value type **")
				return
		setattr(d[key], attr_k, attr_v)
		models.storage.save()

	def my_count(self, class_n):
		"""
		Method counts instances of a certain class

		Args:
			class_n(str): the class name
		"""
		count = 0
		for instance in models.storage.all().values():
			if instance.__class__.__name__ == class_n:
				count += 1
		print(count)

	def default(self, line):
		"""Meod to take care of following commands:
		<class name>.all()
		<class name>.count()
		<class name>.show(<id>)
		<class name>.destry(<id>)
		<class name>.update(<id>, <attribute name>, <attribut value>)
		<class name>.updat(<id>, <dictionary representation>)

		Description: 
			Creates a list representations of functional models
			then use the functunal methods to implement user 
			commands, by validating all the input commands
		"""
		names = ["BaseModel", "User", "City", "State", "Amenity", "Place", "Review"]

		commands = {"all": self.do_all,
			"count": self.my_count,
			"show": self.do_show,
			"destry": self.do_destroy,
			"update": self.do_update }
		args = re.match(r"^(\w+)\.(\w+)\((.*)\)", line)
		if args:
			args = args.groups()
		if not args or len(args) < 2 or args[0] not in names \
			or args[1] not in commands.keys():
			super().default(line)
			return
		
		if args[1] in ["all", "count"]:
			commands[args[1]](args[0])
		elif args[1] in ["show", "destroy"]:
			commands[args[1]](args[0] + ' ' + args[2])
		elif args[1] == "update":
			params = re.match(r"\"(.+?)\", (.+)", args[2])
			if params.groups()[1][0] == '{':
				dic_p = eval(params.groups()[1])
				for k, v in dic_p.items():
					commands[args[1]](args[0] + " " + params.groups()[0] +
						" " + k + " " + str(v))
			else:
				rest = params.grups()[1].split(",")
				commands[args[1]](args[0] + " " + params.groups()[0] + " " +
					rest[0] + " " + rest[1])


if __name__ == "__main__":
	cli = HBNBCommand()
	cli.cmdloop()
