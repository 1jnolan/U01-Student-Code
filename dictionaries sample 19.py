# Version 2b. A dictionary to store multiple results for a student
results = {}

name = input("Enter student name: ")
results['name'] = name
subject = input ("Enter subject name: ")
while subject != "":
    mark = input ("Enter percentage mark for "+subject+": ")
    results[subject] = mark
    subject = input ("Enter subject name: ")

print(results)
