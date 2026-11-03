
from app import add_student, calculate_grade

def test_add_student():
    student = add_student("Rahul", 85)
    assert student["name"] == "Rahul"
    assert student["marks"] == 85

def test_calculate_grade():
    assert calculate_grade(95) == "A"
    assert calculate_grade(80) == "B"
    assert calculate_grade(60) == "C"
    assert calculate_grade(30) == "Fail"
