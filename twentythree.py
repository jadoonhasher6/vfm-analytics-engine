import pandas as pd
students=[
    {"name": "Ali",    "subject": "Math",    "marks": 85},
    {"name": "Sara",   "subject": "English", "marks": 90},
    {"name": "Bilal",  "subject": "Math",    "marks": 78},
    {"name": "Ayesha", "subject": "English", "marks": 88},
    {"name": "Usman",  "subject": "Math",    "marks": 92},
    {"name": "Sara",   "subject": "Science", "marks": 76},
]
df=pd.DataFrame(students)
print(df.groupby('subject')['marks'].agg(['max','min','mean']))
