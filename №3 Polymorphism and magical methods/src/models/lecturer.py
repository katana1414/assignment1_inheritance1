from .mentor import Mentor

class Lecturer(Mentor):
    def __init__(self, name: str, surname: str):
        super().__init__(name, surname)
        self.grades = {}  # курс -> список оценок

    def average_grade(self) -> float:
        all_grades = [g for grades in self.grades.values() for g in grades]
        return sum(all_grades) / len(all_grades) if all_grades else 0.0

    def __str__(self) -> str:
        return (
            f"Имя: {self.name}\n"
            f"Фамилия: {self.surname}\n"
            f"Средняя оценка за лекции: {self.average_grade():.1f}"
        )

    def __lt__(self, other):
        if not isinstance(other, Lecturer):
            return NotImplemented
        return self.average_grade() < other.average_grade()
src/models/reviewer.py
from .mentor import Mentor

class Reviewer(Mentor):
    def __init__(self, name: str, surname: str):
        super().__init__(name, surname)
        self.grades = {}  # курс -> список оценок (для примера)

    def rate_hw(self, student, course: str, grade: int) -> str:
        # рецензент ставит оценку за ДЗ студента
        if course not in self.courses_attached:
            return 'Ошибка'
        if course not in getattr(student, 'courses_in_progress', []) and \
           course not in getattr(student, 'finished_courses', []):
            return 'Ошибка'
        student.grades.setdefault(course, []).append(grade)
        return 'Оценка поставлена'

    def __str__(self) -> str:
        # для примера возьмём среднюю оценку из self.grades, если есть
        all_grades = [g for grades in self.grades.values() for g in grades]
        avg = sum(all_grades) / len(all_grades) if all_grades else 0.0
        return (
            f"Имя: {self.name}\n"
            f"Фамилия: {self.surname}\n"
            f"Средняя оценка за лекции: {avg:.1f}"
        )
