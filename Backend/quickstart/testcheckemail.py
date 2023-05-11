import json

# Open the JSON file
with open('../data/students.json') as f:
    data = json.load(f)

# Search for the student with the specified email
email_to_find = "62050232@kmitl.ac.th"
for student in data:
    if student["email"] == email_to_find:
        print("Found student:", student)
        break
else:
    print("Student with email", email_to_find, "not found")