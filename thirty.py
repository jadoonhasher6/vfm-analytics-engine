import pandas as pd
students = pd.DataFrame([
    {"student_id": 1, "name": "Ali",    "city": "Lahore"},
    {"student_id": 2, "name": "Sara",   "city": "Karachi"},
    {"student_id": 3, "name": "Bilal",  "city": "Islamabad"},
    {"student_id": 4, "name": "Ayesha", "city": "Peshawar"},
])

grades = pd.DataFrame([
    {"student_id": 1, "subject": "Math",    "marks": 85},
    {"student_id": 2, "subject": "Math",    "marks": 90},
    {"student_id": 3, "subject": "Math",    "marks": 78},
])

merged=pd.merge(students,grades,on='student_id',how='left')
print(merged)
