from src.models.student import Student
from src.models.lecturer import Lecturer
from src.models.reviewer import Reviewer
from src.utils.averages import (
    average_student_grades_by_course,
    average_lecturer_grades_by_course,
)

def demo():
    # создаём 2 студентов
    s1 = Student('Анна', 'Смирнова')
    s2 = Student('Игорь', 'Петров')

    # создаём 2 лектора
    l1 = Lecturer('Мария', 'Козлова')
    l2 = Lecturer('Павел', 'Сидоров')

    # создаём 2 рецензента
    r1 = Reviewer('Кирилл', 'Иванов')
    r2 = Reviewer('Елена', 'Смирнова')

    # назначаем курсы
    courses = ['Python', 'Java']
    s1.courses_in_progress += courses
    s2.courses_in_progress += courses
    l1.courses_attached += courses
    l2.courses_attached += courses
    r1.courses_attached += courses
    r2.courses_attached += courses

    # студенты ставят оценки лекторам
    s1.rate_lecture(l1, 'Python', 9)
    s2.rate_lecture(l1, 'Python', 8)
    s1.rate_lecture(l2, 'Java', 7)
    s2.rate_lecture(l2, 'Java', 10)

    # рецензенты ставят оценки за ДЗ
    r1.rate_hw(s1, 'Python', 8)
    r2.rate_hw(s2, 'Python', 9)
    r1.rate_hw(s1, 'Java', 7)
    r2.rate_hw(s2, 'Java', 8)

    print(s1)
    print(s2)
    print(l1)
    print(l2)

    avg_students_python = average_student_grades_by_course([s1, s2], 'Python')
    avg_lecturers_python = average_lecturer_grades_by_course([l1, l2], 'Python')

    print(f'Средняя по Python среди студентов: {avg_students_python:.2f}')
    print(f'Средняя по Python среди лекторов: {avg_lecturers_python:.2f}')

if __name__ == '__main__':
    demo()
