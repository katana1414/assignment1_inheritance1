class Student:
    def __init__(self, name: str, surname: str):
        self.name = name
        self.surname = surname
        self.courses_in_progress = []
        self.finished_courses = []
        self.grades = {}  # курс -> список оценок

    def rate_lecture(self, lecturer, course: str, grade: int):
        # студент ставит оценку лектору за курс
        if course not in self.courses_in_progress:
            return 'Ошибка'
        if course not in getattr(lecturer, 'courses_attached', []):
            return 'Ошибка'
        lecturer.grades.setdefault(course, []).append(grade)
        return 'Оценка поставлена'

    def average_grade(self) -> float:
        all_grades = [g for grades in self.grades.values() for g in grades]
        return sum(all_grades) / len(all_grades) if all_grades else 0.0

    def __str__(self) -> str:
        return (
            f"Имя: {self.name}\n"
            f"Фамилия: {self.surname}\n"
            f"Средняя оценка за домашние задания: {self.average_grade():.1f}\n"
            f"Курсы в процессе изучения: {', '.join(self.courses_in_progress)}\n"
            f"Завершенные курсы: {', '.join(self.finished_courses)}"
        )

    def __lt__(self, other):
        if not isinstance(other, Student):
            return NotImplemented
        return self.average_grade() < other.average_grade()
