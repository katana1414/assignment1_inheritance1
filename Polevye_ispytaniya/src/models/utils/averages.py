def average_student_grades_by_course(students, course: str) -> float:
    # средняя по очкам домашних заданий со всех студентов по заданному курсу
    grades = []
    for s in students:
        grades.extend(s.grades.get(course, []))
    return sum(grades) / len(grades) if grades else 0.0

def average_lecturer_grades_by_course(lecturers, course: str) -> float:
    # средняя по оценкам лекторов по заданному курсу
    grades = []
    for l in lecturers:
        grades.extend(l.grades.get(course, []))
    return sum(grades) / len(grades) if grades else 0.0
