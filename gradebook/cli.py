import argparse
from .models import Student, GradeBook
from .io.csvio import read_students_from_csv

def build_default_gradebook():
    gb = GradeBook()
    gb.add_student(Student("Alice", [90, 85, 92]))
    gb.add_student(Student("Bob",   [70, 75, 68]))
    return gb

def print_report(gb):
    print("전체 반 평균 점수:", round(gb.class_average(), 2))
    for s in gb.students:
        print(f"{s.name} - 평균: {s.average():.1f}, 학점: {s.grade()}")

def main():
    parser = argparse.ArgumentParser(description="GradeBook CLI")
    parser.add_argument("--csv", help="학생 데이터 CSV 경로 (예: data/students.csv)")
    args = parser.parse_args()

    if args.csv:
        gb = read_students_from_csv(args.csv)
    else:
        gb = build_default_gradebook()

    print_report(gb)
