class Matrix(object):
	def __init__(self, matrix_string):
		self.matrix = [list(map(int, rows.split(' '))) for rows in matrix_string.split('\n')]

	def row(self, index):
		index -= 1
		return self.matrix[index]
	def column(self, index):
		index -= 1
		return [i[index] for i in self.matrix]