'''
    script: gradeText.py
    action: a. stores any number of grades into grade.txt
            b. reads grades from grades.txt displayes the individual grades and their total, count and average
            c. enters first and last name as strings and students three exam grades ans integers in grades.csv file
    author: Greyson Dunevant
    date: 12/05/2024          
'''

with open('grades.txt', mode = 'w') as file:
    while True:
        grade = input("Enter a grade (or input '-1' to quit): ")
        if grade.lower() == '-1':
            break
        file.write(grade + '\n')
with open('grades.txt', mode = 'r') as file:
    grades = file.read().split()
    grades = [float(grade) for grade in grades]

    print("Individual grades: ", grades)

    total = sum(grades)
    count = len(grades)
    average = total/count

    print("Total: ", total)
    print("Count: ", count)
    print("Average: ", average)
import csv

with open('grades.csv', mode = 'w') as file:
    writer = csv.writer(file)
    writer.writerow(['First Name', 'Last Name', 'Exam 1', 'Exam 2', 'Exam 3'])

    while True:
        firstName = input("Enter the student's first name ('input 'q' to quit): ")
        if firstName.lower() == 'q':
            break
        lastName = input("Enter the student's last name: ")
        exam1 = int(input("Enter the student's exam 1 grade: "))
        exam2 = int(input("Enter the student's exam 2 grade: "))
        exam3 = int(input("Enter the student's exam 3 grade: "))

        writer.writerow([firstName, lastName, exam1, exam2, exam3])
        
