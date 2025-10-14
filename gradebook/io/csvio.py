import csv
from ..models import Student, GradeBook

def read_students_from_csv(path):
    """CSV: name,score1,score2,..."""
    gb = GradeBook()
    with open(path, newline="", encoding="utf-8") as f:
        reader = csv.reader(f)
        header = next(reader, None)  # 첫 행이 헤더면 건너뛰기
        for row in reader:
            if not row:
                continue
            name = row[0].strip()
            scores = [float(x) for x in row[1:] if x.strip() != ""]
            gb.add_student(Student(name, scores))
    return gb

def write_students_to_csv(path, students):
    """학생 리스트를 CSV로 저장"""
    # 가장 긴 점수 개수에 맞춰 헤더 만들기
    max_len = max((len(s.scores) for s in students), default=0)
    header = ["name"] + [f"score{i+1}" for i in range(max_len)]
    with open(path, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(header)
        for s in students:
            row = [s.name] + s.scores + [""] * (max_len - len(s.scores))
            writer.writerow(row)
