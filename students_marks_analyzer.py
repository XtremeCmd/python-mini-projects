# dictionary for students
students = {}


num_students = int(input("Enter number of students: "))

for _ in range(num_students):
    name = input("\nEnter student name: ")
    subjects = set()  # to avoid duplicates
    marks_data = []   # list of tuples
    
    num_subjects = int(input("Enter number of subjects: "))
    for _ in range(num_subjects):
        subject = input("Subject name: ")
        if subject in subjects:
            print("Duplicate subject ignored!")
            continue
        subjects.add(subject)
        marks = int(input(f"Marks in {subject}: "))
        marks_data.append((subject, marks))
    
    students[name] = marks_data

# Student report
print("\n--- Student Reports ---")
for name, data in students.items():
    total = sum(mark for _, mark in data)
    avg = total / len(data)
    print(f"{name}: Average = {avg:.2f}")

# Finding topper
topper = max(students.items(), key=lambda s: sum(mark for _, mark in s[1]) / len(s[1]))
print(f"\n Topper: {topper[0]} with average {sum(mark for _, mark in topper[1]) / len(topper[1]):.2f}")
