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

from collections import OrderedDict

class Polymer:

	ORIG_POLYMER_STR = ''
	ORIG_POLYMER_DICT = OrderedDict()
	WORKING_POLYMER_DICT = {}
	NEW_POLYMER_STR = ''


	@classmethod
	def create_dict(cls):
		with open('polymers') as f:
			Polymer.ORIG_POLYMER_STR = f.read()
		for k, v in enumerate(Polymer.ORIG_POLYMER_STR):
			Polymer.ORIG_POLYMER_DICT[k] = v
		Polymer.WORKING_POLYMER_DICT = Polymer.ORIG_POLYMER_DICT.copy()

	@classmethod
	def polymer_checker(cls, str):
		i = 1
		reduced = 0
		skip = False
		for k, v in Polymer.WORKING_POLYMER_DICT.items():
			if skip:
				skip = False
				continue
			chars = ''
			chars += v
			if not Polymer.WORKING_POLYMER_DICT.get(i):
				break
			chars += Polymer.WORKING_POLYMER_DICT.get(i)
			print(chars)
			if (any(char.isupper() for char in chars) and any(
				char.islower() for char in chars)) and \
				chars[0].lower() == chars[1].lower():
				skip = True
				i += 2
				reduced += 1
				continue
			else:
				Polymer.NEW_POLYMER_STR += chars
				i += 1
		if reduced:
			Polymer.polymer_checker(Polymer.NEW_POLYMER_STR)


Polymer.create_dict()
print(Polymer.WORKING_POLYMER_DICT)
Polymer.polymer_checker(Polymer.ORIG_POLYMER_STR)
print(Polymer.NEW_POLYMER_STR)
# Polymer.POLYMER_DICT.pop(0)
# print(Polymer.POLYMER_DICT)








