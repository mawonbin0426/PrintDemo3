from .utils import mean, letter_grade

class Student:
    def __init__(self, name, scores):
        self.name = name
        self.scores = list(scores)

    def average(self):
        return mean(self.scores)

    def grade(self):
        return letter_grade(self.average())

class GradeBook:
    def __init__(self):
        self.students = []

    def add_student(self, student: "Student"):
        self.students.append(student)

    def class_average(self):
        if not self.students:
            return 0.0
        return sum(s.average() for s in self.students) / len(self.students)
