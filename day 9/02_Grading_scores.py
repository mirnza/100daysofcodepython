student_scores = {
    "Harry": 81,
    "Ron": 78,
    "Hermoine": 99,
    "Draco": 74,
    "Neville": 62
}

Student_Grades = {}
for student in student_scores:
    score = student_scores[student]
    if score > 90:
        Student_Grades[student] = "Outstanding"
    elif score > 80:
        Student_Grades[student] = "Exceeds Expectation"
    elif score > 70:
        Student_Grades[student] = "Acceptable"
    else:
        Student_Grades[student] = "Fail"

print(Student_Grades) 