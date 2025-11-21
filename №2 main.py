from src.models.student import Student
from src.models.lecturer import Lecturer
from src.models.reviewer import Reviewer

def main_demo():
    # создание участников
    student = Student('Алексей', 'Иванов')
    lecturer = Lecturer('Иван', 'Иванов')
    reviewer = Reviewer('Пётр', 'Петров')

    # назначение курсов
    student.courses_in_progress += ['Python', 'Java']
    lecturer.courses_attached += ['Python', 'C++']
    reviewer.courses_attached += ['Python', 'Java']

    # сценарий использования
    print(student.rate_lecture(lecturer, 'Python', 9))     # Оценка поставлена
    print(student.rate_lecture(lecturer, 'Java', 8))       # Ошибка (Java не прикреплён лектору)
    print(reviewer.rate_hw(student, 'Python', 8))          # Оценка за ДЗ поставлена
    print(student)

    print(lecturer)

if __name__ == "__main__":
    main_demo()
