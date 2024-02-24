#!/usr/bin/python3
"""Module of a base class.
"""


class Base:
	"""Base class of all other classes in this project.

	Attributes:
		__nb_objects (int) : objects of base.
	"""

	def __init__(self, id=None):
		"""Initialize Base object.

		Args:
		id (int, optional): ID of the object. Defaults to None.
		"""
		if id is not None:
			self.id = id
		else:
			Base.__nb_objects += 1
			self.id = Base.__nb_objects
