# AirBnB clone


##Description of the Project

This is my AirBnB clone project that was completed to test my skills on the software engineering concepts I have beeen studying for the passed 5 months. The goal of the project is to deploy a working replica of AirBnB website on my servert. The final version of the project will have;
- A command interpreter to manipulate data without a visual interface, like a shell (for development and debugging)
- A website (front-end) with static and dynamic functionalities
- A comprehensive database to manage the backend functionalities
- An API that provides a communication interface between the front and backend of the system.

##Concepts in Review

* How to create a Python package
* How to create a command interpreter in Python using the cmd module
* What is Unit testing and how to implement it in a large project
* How to serialize and deserialize a Class
* How to write and read a JSON file
* How to manage datetime
* What is an UUID
* What is *args and how to use it
* What is **kwargs and how to use it
* How to handle named arguments in a function

##Description of the Command Interpreter
Commands	Description
quit	Quits the console
Ctrl+D	Quits the console
help or help <command>	Displays all commands or Displays instructions for a specific command
create <class>	Creates an object of type , saves it to a JSON file, and prints the objects ID
show <class> <ID>	Shows string representation of an object
destroy <class> <ID>	Deletes an objects
all or all <class>	Prints all string representations of all objects or Prints all string representations of all objects of a specific class
update <class> <id> <attribute name> "<attribute value>"	Updates an object with a certain attribute (new or existing)
<class>.all()	Same as all <class>
<class>.count()	Retrieves the number of objects of a certain class
<class>.show(<ID>)	Same as show <class> <ID>
<class>.destroy(<ID>)	Same as destroy <class> <ID>
<class>.update(<ID>, <attribute name>, <attribute value>	Same as update <class> <ID> <attribute name> <attribute value>
<class>.update(<ID>, <dictionary representation>)	Updates an objects based on a dictionary representation of attribute names and values
The shell interpreter will work both in interactive and non interactive mode

In interactive mode, this is how it how you start it and how you use it:

$ ./console.py
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF  help  quit

(hbnb) 
(hbnb) 
(hbnb) quit
$

In noninteractive mode, the shell works like this

$ echo "help" | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb) 
$
$ cat test_help
help
$
$ cat test_help | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb) 
$
