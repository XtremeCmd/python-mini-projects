num = int(input('Enter number of students: '))
data = [tuple(input("Enter name and score: ").split()) for i in range(num)]

grades = [
    (name, 
     'A+' if int(score) >= 90 else 
     'A' if int(score) >= 80 else 
     'B' if int(score) >= 70 else 
     'C' if int(score) >= 50 else 
     'F')
    for name, score in data
]

print("Grades:")
print(grades)