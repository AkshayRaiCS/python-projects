import csv
students = []

with open("names.csv") as file:
    reader = csv.DictReader(file)
    for row in reader:
        students.append(row)
#can use lambda, like key=lambda student: students["name"]
for student in sorted(students,key=lambda students: students["name"]):
    print(f"{student['name']} is in {student['home']}")



