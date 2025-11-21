from src.models.student import Student
from src.models.lecturer import Lecturer
from src.models.reviewer import Reviewer

def demo():
    # участники
    s1 = Student('Иван', 'Иванов')
    s2 = Student('Мария', 'Петрова')

    l1 = Lecturer('Анна', 'Кузнецова')
    l2 = Lecturer('Дмитрий', 'Смирнов')

    r1 = Reviewer('Петр', 'Сидоров')
    r2 = Reviewer('Елена', 'Фролова')

    # курсы
    s1.courses_in_progress += ['Python', 'Git']
    s2.courses_in_progress += ['Python', 'Git']

    l1.courses_attached += ['Python', 'Git']
    l2.courses_attached += ['Python', 'Git']

    r1.courses_attached += ['Python', 'Git']
    r2.courses_attached += ['Python', 'Git']

    # ставим оценки
    s1.rate_lecture(l1, 'Python', 9)
    s2.rate_lecture(l1, 'Python', 8)
    s1.rate_lecture(l2, 'Git', 10)
    s2.rate_lecture(l2, 'Git', 9)

    r1.rate_hw(s1, 'Python', 8)
    r2.rate_hw(s2, 'Python', 9)
    r1.rate_hw(s1, 'Git', 7)
    r2.rate_hw(s2, 'Git', 8)

    print(s1)
    print()
    print(s2)
    print()
    print(l1)
    print()
    print(l2)
    print()
    print(r1)
    print(r2)

    # сравнения
    print("\nСравнение студентов по среднему за ДЗ:")
    print(s1 < s2)

    print("Сравнение лекторов по среднему за лекции:")
    print(l1 < l2)

if __name__ == '__main__':
    demo()
