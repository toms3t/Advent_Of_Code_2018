# 1. Import polymer string as enumerate dictionary
# 2. Make a copy of the dictionary
# 3. Iterate through the dictionary and remove same type, opposite polarity units
# 4. Make additional passes through the dictionary until there are no more reductions
# 5. Count remaining units


# 1. Import polymer string as enumerate dictionary
# 2. Make a copy of the dictionary
# 3. Iterate through the dictionary and create new dict with compatible units
# 4. Make additional passes through the dictionary until there are no more reductions
# 5. Count remaining units


#class Polymer
#functions
# import string into enumerate dict
# polymer unit checker (determine if units react or not)
# iterator that goes through the enumerate dict and runs polymer-unit-checker on it
# counts units in new dict

# Evaluate first two characters (first=True)
# If both are valid, add to string, iterate (addtostr=True)
# else if both are destroyed, do not add to string and remove last char (addtostr=False)
# Next two characters --
# If characters don't react, only add the second character if addtostr=True
# else if both are destroyed, do not add to string and remove last char (addtostr=False)

from collections import OrderedDict
from string import ascii_lowercase


class Polymer:

	ORIG_POLYMER_STR = ''
	ORIG_POLYMER_DICT = OrderedDict()
	WORKING_POLYMER_STR = ''
	WORKING_POLYMER_DICT = {}
	NEW_POLYMER_STR = ''
	POLYMER_LENGTH = 0
	PROBLEM_UNIT = ''

	@classmethod
	def read_poly_str(cls):
		with open('polymers') as f:
			Polymer.ORIG_POLYMER_STR = f.read()


	@classmethod
	def create_dict(cls, poly_str):
		if Polymer.ORIG_POLYMER_DICT:
			Polymer.ORIG_POLYMER_DICT.clear()
		for k, v in enumerate(poly_str):
			Polymer.ORIG_POLYMER_DICT[k] = v
		Polymer.WORKING_POLYMER_DICT = Polymer.ORIG_POLYMER_DICT.copy()

	@classmethod
	def polymer_reducer(cls):
		i = 1
		new_str = ''
		reduced = 0
		add_to_str = False
		skip = False
		for k, v in Polymer.WORKING_POLYMER_DICT.items():
			if skip:
				skip = False
				continue
			chars = ''
			chars += v
			if not Polymer.WORKING_POLYMER_DICT.get(i):
				if not add_to_str:
					new_str += chars
				break
			chars += Polymer.WORKING_POLYMER_DICT.get(i)
			if chars[0].lower() != chars[1].lower():
				if add_to_str:
					new_str += chars[-1]
				else:
					new_str += chars
				i += 1
				add_to_str = True
			elif not (any(char.isupper() for char in chars)):
				if add_to_str:
					new_str += chars[-1]
				else:
					new_str += chars
				i += 1
				add_to_str = True
			elif not (any(char.islower() for char in chars)):
				if add_to_str:
					new_str += chars[-1]
				else:
					new_str += chars
				i += 1
				add_to_str = True
			elif (any(char.isupper() for char in chars) and any(
				char.islower() for char in chars)) and \
				chars[0].lower() == chars[1].lower():
				skip = True
				i += 2
				reduced += 1
				if add_to_str:
					new_str = new_str[:-1]
				add_to_str = False
				continue
			else:
				new_str += chars
				i += 1
		Polymer.NEW_POLYMER_STR = new_str
		# print(new_str)
		if reduced:
			Polymer.create_dict(Polymer.NEW_POLYMER_STR)
			Polymer.polymer_reducer()
		# Polymer.POLYMER_LENGTH = len(Polymer.NEW_POLYMER_STR)

	@classmethod
	def unit_remover(cls, char):
		Polymer.WORKING_POLYMER_STR = ''.join([
			x for x in Polymer.ORIG_POLYMER_STR
			if (x != char and x != char.upper())
		]
		)

	@classmethod
	def problem_unit_finder(cls):
		problem_unit_tracker = {}
		for char in ascii_lowercase:
			# char = 'z'
			Polymer.unit_remover(char)
			# print(Polymer.WORKING_POLYMER_STR)
			Polymer.create_dict(Polymer.WORKING_POLYMER_STR)
			try:
				Polymer.polymer_reducer()
			except:
				continue
			problem_unit_tracker[char] = Polymer.NEW_POLYMER_STR
			print(char, len(Polymer.NEW_POLYMER_STR))




Polymer.read_poly_str()
Polymer.problem_unit_finder()
# Polymer.create_dict(Polymer.ORIG_POLYMER_STR)
# print(Polymer.WORKING_POLYMER_STR)
# print(Polymer.WORKING_POLYMER_DICT)
# Polymer.polymer_reducer()
# print(Polymer.NEW_POLYMER_STR)
# print(len(Polymer.NEW_POLYMER_STR))
# # assert ans == Polymer.NEW_POLYMER_STR







