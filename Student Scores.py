student_scores = {
    "Paulo": 80,
    "Rosana": 77,
    "João": 90,
    "Alessandra": 65,
    "José": 60,
}

student_grades={}
for student in student_scores:
    score = student_scores[student]
    if score <90:
        student_grades[student]= "Excellent"
    elif score < 80:
        student_grades[student] = "Very Good"
    elif score < 70:
        student_grades[student] = "Good"
    else:
       student_grades[student] = "Fail"

print(student_grades) 