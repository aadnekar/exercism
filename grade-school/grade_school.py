class School(object):
	def __init__(self):
		self.students = []

	def add_student(self, name, grade):
		self.students.append({'name': name, 'grade': grade})
		return

	def roster(self):
		return [stud['name'] for stud in sorted(self.students, key=lambda stud: (stud['grade'], stud['name']))]

	def grade(self, grade_number):
		return sorted([stud['name'] for stud in filter(lambda stud: stud['grade'] == grade_number, self.students)])
