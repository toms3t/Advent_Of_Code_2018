# functions

# read in coordinates into list of tuples
# Draw map (coordinates and proximity letters) - also use this to draw basic map using max coordinates
# apply Manhattan distance
# find largest area

# from itertools import product
# coordinates = list(product(xrange(width), xrange(height)))
from string import ascii_lowercase, punctuation


class ChronalMap:

	def __init__(self, coordinates):
		self.coordinates = coordinates
		self.map = []
		self.largest_x = 0
		self.largest_y = 0
		self.chars = ascii_lowercase + punctuation.replace('.', '').replace(',', '')
		self.char_dict = {}
		self.distance_tracker = {}
		self.before_after_dict = {}
		self.nearest_char_per_coordinate = {}

	@classmethod
	def from_coordinates_file(cls, f):
		with open(f) as f:
			f = f.readlines()
			coordinates = [tuple(x.split(',')) for x in f]
			coordinates = [(int(x[0]), int(x[1].strip('\n'))) for x in coordinates]
			return cls(coordinates)

	def determine_map_area(self):
		for item in self.coordinates:
			if item[0] > self.largest_x:
				self.largest_x = item[0]
			if item[1] > self.largest_y:
				self.largest_y = item[1]+1

	def draw_map(self, x, y):
		if not self.map:
			self.map = [
				[i, j] for j in range(y)
				for i in range(x+1)
			]
		enum_dict = {k: v for k, v in enumerate(self.map)}
		print(enum_dict)
		for num, coordinate in enum_dict.items():
			if isinstance(coordinate[0], int):
				if coordinate[0] < self.largest_x:
					print('.', end=' ')
				elif coordinate[0] == self.largest_x:
					print('.')
			else:
				if num % self.largest_x == self.largest_x:
					print(coordinate[0])
				else:
					print(coordinate[0], end=' ')
		print('\n')

	def add_coordinate_characters_to_map(self):
		char = self.character_generator()
		for coordinate in self.coordinates:
			ind = ((self.largest_x+1) * coordinate[1]) + coordinate[0]
			self.map[ind][0] = next(char)[0]

	def create_char_dict(self):
		self.char_dict = {v: k for k, v in enumerate(self.chars)}

	def character_generator(self):
		for k, v in self.char_dict.items():
			yield (k, v)

	def create_before_after_dict(self):
		before_counter = 0
		after_counter = 0
		char = ''
		for coordinate in self.map:
			if isinstance(coordinate[0], str):
				char = coordinate[0]
				before_counter = 1
			if isinstance(coordinate[0], int):
				self.before_after_dict[''.join(str(coordinate))] = []
				if before_counter % 20 == 0:
					self.before_after_dict[''.join(str(coordinate))].append(
						{char: 2}
					)
				else:
					self.before_after_dict[''.join(str(coordinate))].append(
						{char: before_counter % 20}
					)
					before_counter += 1
		for coordinate in self.map[::-1]:
			if isinstance(coordinate[0], str):
				char = coordinate[0]
				after_counter = 1
			if isinstance(coordinate[0], int):
				if after_counter % 20 == 0:
					self.before_after_dict[''.join(str(coordinate))].append(
						{char: 2}
					)
				else:
					self.before_after_dict[''.join(str(coordinate))].append(
						{char: after_counter % 20}
					)
					after_counter += 1

	# PROBLEM : nearest character may not be the "before" or "after" character

	# def calc_manhattan_distance(self):
	# 	for coordinate in self.map:
	# 		distances = self.before_after_dict.get(''.join(str(coordinate)))
	# 		self.nearest_char_per_coordinate[coordinate] =
	# 		print(distances)



	# def add_nearest_char_to_map(self):
	# 	for coordinate in self.map:
	# 		if isinstance(coordinate[0], int):


# for each coordinate, if it's a dot, find distance before to nearest char and
# distance after to the nearest char, -- if char, skip.
	# functions - find before, find after
	# dictionary - coordinate_of_dot: (before, after)
# with before and after numbers, determine which is closer
	# functions - calc_distance
# draw map to replace dots with nearest char
	# functions - add_char_to_map
# determine which chars have a finite area and return largest
	# functions - find_finite_areas, find_largest_area

#   '[0, 2]': [20, 1], '[3, 2]': [1, 7]






a = ChronalMap.from_coordinates_file('coordinates2')
a.determine_map_area()
a.draw_map(a.largest_x, a.largest_y)
a.create_char_dict()
a.add_coordinate_characters_to_map()
print(a.map)
a.draw_map(a.largest_x, a.largest_y)
a.create_before_after_dict()
print(a.before_after_dict)
# a.calc_manhattan_distance()




# a.map[79][0] = 'C'
# coordinate 0,1 = a.map[(a.largest_y*y)+x][0] (12+0)   (((largest x+1) * y) + x)
# coordinate 1,1 = a.map[(a.largest_y*y)+x][0] (12+1)   (12 * 1) + x
# coordinate 1,6 = a.map[(a.largest_y*y)+x][0] (12*6)+1 (13 * 6) + 1
# coordinate 3,6 = a.map[(a.largest_y*y)+x][0] (12*6)+3 (13 * 6) + 3
# coordinate 3,7 = a.map[(a.largest_y*y)+x][0] (12*6)+3 (13 * 7) + 3

