students=[
     {"name": "Ali",   "subject": "Math",    "marks": 85},
    {"name": "Sara",  "subject": "English", "marks": 90},
    {"name": "Bilal", "subject": "Math",    "marks": 78},
    {"name": "Ayesha","subject": "English", "marks": 88},
    {"name": "Usman", "subject": "Math",    "marks": 92},
    {"name": "Sara",  "subject": "Science", "marks": 76},
]
import pandas as pd
df=pd.DataFrame(students)
df['passed']=df['marks']>=80
print(df.groupby('subject')['passed'].sum())