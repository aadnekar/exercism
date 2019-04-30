PLANTS = {'C': 'Clover', 'G': 'Grass', 'R': 'Radishes', 'V': 'Violets'}

class Garden(object):
    def __init__(self, diagram, students=None):
        self.diagram = diagram.split('\n')
        if students is None:
            self.students = {'Alice': 0, 'Bob': 1, 'Charlie': 2, 'David': 3,
                             'Eve': 4, 'Fred': 5, 'Ginny': 6, 'Harriet': 7,
                             'Ileana': 8, 'Joseph': 9, 'Kincaid': 10, 'Larry': 11}
        else:
            self.students = {}
            for position, student in enumerate(students):
                print("position: {}, student: {}".format(position, student))
                self.students[student] = position

    def plants(self, student):
        position = self.students[student] * 2
        return [PLANTS[self.diagram[0][position]], PLANTS[self.diagram[0][position+1]], PLANTS[self.diagram[1][position]], PLANTS[self.diagram[1][position+1]]]
