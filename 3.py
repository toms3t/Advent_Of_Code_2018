import re


class Claim:
	def __init__(self, num, x, y, width, height):
		self.num = num
		self.x = int(x)
		self.y = int(y)
		self.width = int(width)
		self.height = int(height)
		self.planned_claim_area = int(width)*int(height)
		Claim.CLAIM_OVERLAP_DICT[self.num] = [self.planned_claim_area]

	with open('claim_list', 'r') as f:
		CLAIM_LIST = f.readlines()

	MATRIX = [['.' for _ in range(1000)] for _ in range(1000)]
	OVERLAP_COUNT = 0
	CLAIM_OVERLAP_DICT = {}

	@classmethod
	def from_file(cls, claim_str):
		regex_pattern = re.compile('#(\d+) @ (\d+),(\d+): (\d+)x(\d+)')
		num, x, y, width, height = \
			regex_pattern.match(claim_str).group(1, 2, 3, 4, 5)
		return cls(num, x, y, width, height)

	def overlap_counter(self, _id):
		y_incrementer = 0
		for _ in range(claimObj.height):
			x_incrementer = 0
			for _ in range(claimObj.width):
				try:
					if claimObj.MATRIX[self.y + y_incrementer][
						self.x + x_incrementer].isdigit():
						claimObj.MATRIX[self.y + y_incrementer][
							self.x + x_incrementer] = 'X'
						Claim.OVERLAP_COUNT += 1
					elif claimObj.MATRIX[self.y + y_incrementer][
						self.x + x_incrementer] == '.':
						claimObj.MATRIX[self.y + y_incrementer][
							self.x + x_incrementer] = claimObj.num
				except IndexError:
					continue
				x_incrementer += 1
			y_incrementer += 1

	@classmethod
	def complete_claim_finder(cls, _id):
		count = 0
		for row in Claim.MATRIX:
			for inch in row:
				if inch == _id:
					count += 1
		Claim.CLAIM_OVERLAP_DICT[_id].append(count)
		if Claim.CLAIM_OVERLAP_DICT[_id][0] == Claim.CLAIM_OVERLAP_DICT[_id][1]:
			return _id


for _id in Claim.CLAIM_LIST:
	claimObj = Claim.from_file(_id)
	claimObj.overlap_counter(_id)

non_overlap_claim = ''
for claim in Claim.CLAIM_OVERLAP_DICT:
	if Claim.complete_claim_finder(claim):
		non_overlap_claim = Claim.complete_claim_finder(claim)

print('Part 1 answer is: {}'.format(Claim.OVERLAP_COUNT))
print('Part 2 answer is: {}'.format(non_overlap_claim))


