mark1 = input("Enter marks for subject 1 (or type 'Absent'): ")
mark2 = input("Enter marks for subject 2 (or type 'Absent'): ")
mark3 = input("Enter marks for subject 3 (or type 'Absent'): ")


if mark1.lower() != 'absent':
    mark1 = int(mark1)
if mark2.lower() != 'absent':
    mark2 = int(mark2)
if mark3.lower() != 'absent':
    mark3 = int(mark3)


total = 0
count = 0
fail = False

if mark1 == 'Absent':
    grade1 = 'NA'
    fail = True
else:
    if mark1 <= 39:
        grade1 = 'F'
        fail = True
    elif mark1 <= 44:
        grade1 = 'P'
    elif mark1 <= 49:
        grade1 = 'C'
    elif mark1 <= 54:
        grade1 = 'B'
    elif mark1 <= 59:
        grade1 = 'B+'
    elif mark1 <= 69:
        grade1 = 'A'
    elif mark1 <= 79:
        grade1 = 'A+'
    else:
        grade1 = 'O'
    total += mark1
    count += 1


if mark2 == 'Absent':
    grade2 = 'NA'
    fail = True
else:
    if mark2 <= 39:
        grade2 = 'F'
        fail = True
    elif mark2 <= 44:
        grade2 = 'P'
    elif mark2 <= 49:
        grade2 = 'C'
    elif mark2 <= 54:
        grade2 = 'B'
    elif mark2 <= 59:
        grade2 = 'B+'
    elif mark2 <= 69:
        grade2 = 'A'
    elif mark2 <= 79:
        grade2 = 'A+'
    else:
        grade2 = 'O'
    total += mark2
    count += 1


if mark3 == 'Absent':
    grade3 = 'NA'
    fail = True
else:
    if mark3 <= 39:
        grade3 = 'F'
        fail = True
    elif mark3 <= 44:
        grade3 = 'P'
    elif mark3 <= 49:
        grade3 = 'C'
    elif mark3 <= 54:
        grade3 = 'B'
    elif mark3 <= 59:
        grade3 = 'B+'
    elif mark3 <= 69:
        grade3 = 'A'
    elif mark3 <= 79:
        grade3 = 'A+'
    else:
        grade3 = 'O'
    total += mark3
    count += 1


if count > 0:
    average = total / count
else:
    average = 0


print("\nResults:")
print("Subject 1: Marks =", mark1, ", Grade =", grade1)
print("Subject 2: Marks =", mark2, ", Grade =", grade2)
print("Subject 3: Marks =", mark3, ", Grade =", grade3)
print("Total Marks (excluding Absent):", total)
print("Average Marks:", round(average, 2))
print("Result:", "Fail" if fail else "Pass")
