import csv
from ..models import Student, GradeBook

def read_students_from_csv(path):
    gb = GradeBook()
    with open(path, newline="", encoding="utf-8") as f:
        reader = csv.reader(f)
        header = next(reader, None)
        for row in reader:
            if not row:
                continue
            name = row[0].strip()
            scores = [float(x) for x in row[1:] if x.strip() != ""]
            gb.add_student(Student(name, scores))
    return gb
