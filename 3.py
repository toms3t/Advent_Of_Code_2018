# 1. Parse claims file and use claim details to create data structure
#    Data structure = dictionary -- (ID: [x,y,width,height]
#    or.... uses classes ID.x, ID.y, ID.width, ID.height
# 2. Determine the largest dimension of fabric needed to fit all claims
# 3. Assign a tuple of x,y values for each spot on the matrix as class variable
# 4. Define instance methods - create_claim_dict, draw 2d matrix,
#    draw claim on matrix, and calculate_overlap

# s = re.compile('.(\d+) @ (\d+),(\d+): (\d+)x(\d+)')
# id,x,y,width,height = s.match(a).group(1,2,3,4,5)

class Claims:
	def __init__(self, _id, x, y, width, height):


	def draw_2d_matrix(self):


	def draw_claim_on_matrix(self):


	def calculate_overlap(self):

	@classmethod
	def from_file(cls, claim_str):
		new_claim = Claims()


