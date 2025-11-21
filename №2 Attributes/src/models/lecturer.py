from .mentor import Mentor

class Lecturer(Mentor):
    def __init__(self, name: str, surname: str):
        super().__init__(name, surname)
        self.grades = {}  # dict: курс -> список оценок от студентов

    def average_grade(self) -> float:
        all_grades = [g for grades in self.grades.values() for g in grades]
        return sum(all_grades) / len(all_grades) if all_grades else 0.0

    def __str__(self) -> str:
        return (
            f"Лектор: {self.name} {self.surname}\n"
            f"Средняя оценка: {self.average_grade():.1f}"
        )
