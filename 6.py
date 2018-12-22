# functions

# read in coordinates into list of tuples
# Draw map (coordinates and proximity letters) - also use this to draw basic map using max coordinates
# apply Manhattan distance
# find largest area

# from itertools import product
# coordinates = list(product(xrange(width), xrange(height)))


class ChronalMap:

	def __init__(self, coordinates):
		self.coordinates = coordinates
		self.map = []
		self.largest_x = 0
		self.largest_y = 0

	@classmethod
	def from_coordinates_file(cls, f):
		with open(f) as f:
			f = f.readlines()
			coordinates = [tuple(x.split(',')) for x in f]
			coordinates = [(int(x[0]), int(x[1].strip('\n'))) for x in coordinates]
			return cls(coordinates)

	def draw_map(self, x, y):
		if not self.map:
			self.map = [
				[i, j] for j in range(y)
				for i in range(x)
			]
		enum_dict = dict(enumerate(self.map))
		for num, coordinate in enum_dict.items():
			if isinstance(coordinate[0], int):
				if coordinate[0] < (self.largest_x - 1):
					print('.', end=' ')
				elif coordinate[0] == (self.largest_x - 1):
					print('.')
			else:
				if num == (self.largest_x-1):
					print(coordinate[0])
				else:
					print(coordinate[0], end=' ')



	def calc_manhattan_distance(self):
		pass

	def determine_map_area(self):
		for item in self.coordinates:
			if item[0] > self.largest_x:
				self.largest_x = item[0]
			if item[1] > self.largest_y:
				self.largest_y = item[1]



a = ChronalMap.from_coordinates_file('coordinates')
# print(a.coordinates)
a.determine_map_area()
a.largest_x = 12
a.largest_y = 12
a.draw_map(a.largest_x, a.largest_y)

a.map[18][0] = 'C'
# coordinate 0,1 = a.map[1][0]
# coordinate 1,1 = a.map[a.largest_x+1][0]
# coordinate 1,6 = a.map[a.largest_x+6][0]
# coordinate 3,6 = a.map[a.largest_x+6][0]

print(a.map)
# print(a.map[0][0])
a.draw_map(a.largest_x, a.largest_y)




