from faker import Faker
import sqlite3
import random
import os

import os

if os.path.exists("university.db"):
    os.remove("university.db")


fake = Faker()
conn = sqlite3.connect('university.db')
cursor = conn.cursor()

# Load schema
with open('schema.sql', 'r') as f:
    cursor.executescript(f.read())

# Add groups
groups = ['Group A', 'Group B', 'Group C']
cursor.executemany("INSERT INTO groups (name) VALUES (?)", [(g,) for g in groups])

# Add teachers
teachers = [fake.name() for _ in range(4)]
cursor.executemany("INSERT INTO teachers (name) VALUES (?)", [(t,) for t in teachers])

# Add subjects
subject_names = ['Math', 'Physics', 'Chemistry', 'History', 'Biology', 'Philosophy', 'Art']
subjects = [(name, random.randint(1, 4)) for name in subject_names]
cursor.executemany("INSERT INTO subjects (name, teacher_id) VALUES (?, ?)", subjects)

# Add students
students = [(fake.name(), random.randint(1, 3)) for _ in range(50)]
cursor.executemany("INSERT INTO students (name, group_id) VALUES (?, ?)", students)

# Add grades
student_ids = [row[0] for row in cursor.execute("SELECT id FROM students").fetchall()]
subject_ids = [row[0] for row in cursor.execute("SELECT id FROM subjects").fetchall()]

for student_id in student_ids:
    for _ in range(random.randint(15, 25)):
        subject_id = random.choice(subject_ids)
        grade = random.randint(60, 100)
        date = fake.date_between(start_date='-6M', end_date='today')
        cursor.execute("INSERT INTO grades (student_id, subject_id, grade, date_of) VALUES (?, ?, ?, ?)",
                       (student_id, subject_id, grade, date))

conn.commit()

print("Created database with:")
print("Students:", cursor.execute("SELECT COUNT(*) FROM students").fetchone()[0])
print("Teachers:", cursor.execute("SELECT COUNT(*) FROM teachers").fetchone()[0])
print("Subjects:", cursor.execute("SELECT COUNT(*) FROM subjects").fetchone()[0])
print("Groups:", cursor.execute("SELECT COUNT(*) FROM groups").fetchone()[0])
print("Grades:", cursor.execute("SELECT COUNT(*) FROM grades").fetchone()[0])

conn.close()

