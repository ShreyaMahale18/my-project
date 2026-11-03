
def add_student(name, marks):
    return {
        "name": name,
        "marks": marks
    }

def calculate_grade(marks):
    if marks >= 90:
        return "A"
    elif marks >= 75:
        return "B"
    elif marks >= 50:
        return "C"
    else:
        return "Fail"

if __name__ == "__main__":
    student = add_student("Rahul", 85)

    print("Student Name:", student["name"])
    print("Marks:", student["marks"])
    print("Grade:", calculate_grade(student["marks"]))
