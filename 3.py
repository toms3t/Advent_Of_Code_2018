# 1. Parse claims file and use claim details to create data structure
#    Data structure = dictionary -- (ID: [x,y,width,height]
#    or.... uses classes ID.x, ID.y, ID.width, ID.height
# 2. Determine the largest dimension of fabric needed to fit all claims
# 3. Assign a tuple of x,y values for each spot on the matrix as class variable
# 4. Define instance methods - create_claim_dict, draw 2d matrix,
#    draw claim on matrix, and calculate_overlap


# NO NEED TO DRAW THE 2D MATRIX
# MATRIX is 1000 sq inches (no need to calc the fabric size)
# Next step, draw 1 claim on matrix and imprint size of claim with claim num
import re


class Fabric:
	def __init__(self, num, x, y, width, height):
		self.num = num
		self.x = int(x)
		self.y = int(y)
		self.width = int(width)
		self.height = int(height)

	with open('claims', 'r') as f:
		CLAIMS = f.readlines()

	# MAX_X = 0
	# MAX_Y = 0
	MATRIX = [['.' for _ in range(1000)] for _ in range(1000)]

	# def find_matrix_size(self):
	# 	if self.x+self.width > Fabric.MAX_X:
	# 		Fabric.MAX_X = self.x + self.width
	# 	if self.y+self.height > Fabric.MAX_Y:
	# 		Fabric.MAX_Y = self.y + self.height
	#
	# @classmethod
	# def create_2d_matrix(cls):
	# 	for _ in range(cls.MAX_Y):
	# 		Fabric.MATRIX.append(['.' * cls.MAX_X])
	#
	# @classmethod
	# def draw_2d_matrix(cls):
	# 	for row in cls.MATRIX:
	# 		print(row)


	def draw_claim_on_matrix(self):
		pass

	def calculate_overlap(self):
		pass

	@classmethod
	def from_file(cls, claim_str):
		regex_pattern = re.compile('#(\d+) @ (\d+),(\d+): (\d+)x(\d+)')
		num, x, y, width, height = \
			regex_pattern.match(claim_str).group(1, 2, 3, 4, 5)
		return cls(num, x, y, width, height)

X = 0
for claim in Fabric.CLAIMS:
	claimObj = Fabric.from_file(claim)
	x = claimObj.x
	y = claimObj.y
	y_incrementer = 0
	for _ in range(claimObj.height):
		x_incrementer = 0
		for _ in range(claimObj.width):
			try:
				if claimObj.MATRIX[y + y_incrementer][x + x_incrementer] == '#':
					claimObj.MATRIX[y + y_incrementer][x + x_incrementer] = 'X'
					X += 1
				elif claimObj.MATRIX[y + y_incrementer][x + x_incrementer] == '.':
					claimObj.MATRIX[y + y_incrementer][x + x_incrementer] = '#'
				elif claimObj.MATRIX[y + y_incrementer][x + x_incrementer] == 'X':
					continue
			except IndexError:
				continue
			x_incrementer += 1
		y_incrementer += 1


print('X', X)

# h = 0
# for x in Fabric.MATRIX:
# 	for y in x:
# 		if y != 'X':
# 			print(y)
# 			h += 1
#
# print(h)




#1 @ 432,394: 29x14

