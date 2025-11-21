from src.models.mentor import Lecturer, Reviewer, Mentor

def test_inheritance():
    lecturer = Lecturer('Иван', 'Иванов')
    reviewer = Reviewer('Пётр', 'Петров')

    assert isinstance(lecturer, Mentor)
    assert isinstance(reviewer, Mentor)
    assert lecturer.courses_attached == []
    assert reviewer.courses_attached == []
