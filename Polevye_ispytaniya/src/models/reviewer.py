from .mentor import Mentor

class Reviewer(Mentor):
    def rate_hw(self, student, course: str, grade: int) -> str:
        # рецензент ставит оценку за ДЗ
        if course not in self.courses_attached:
            return 'Ошибка'
        if course not in getattr(student, 'courses_in_progress', []):
            return 'Ошибка'
        student.grades.setdefault(course, []).append(grade)
        return 'Оценка поставлена'
