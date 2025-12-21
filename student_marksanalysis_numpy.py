import numpy as np 
# 3 subjects and 5 students
# row = students, column = marks

marks_arr = np.array([[91, 7, 21],
                    [86, 54, 37],
                    [56, 22, 11],
                    [78, 6, 54],
                    [33, 65, 47]
                    ])

print(f"Maximum marks in class is {marks_arr.max()}")
print(f"Minimum marks in class is {marks_arr.min()}")

#analysis of students

#analysis of first student
print(f'Highest marks of first student is {marks_arr[0].max()}')
print(f'Lowest marks of first student is {marks_arr[0].min()}')
print(f'Total marks of first student is {marks_arr[0].sum()}')
print(f'Average marks of first student is {marks_arr[0].mean()}')
pass_chanceoffirststudent = 0
for mark in marks_arr[0]:
  if mark >= 30:
    pass_chanceoffirststudent += 1

#analysis of second student
print(f'Highest marks of second student is {marks_arr[1].max()}')
print(f'Lowest marks of second student is {marks_arr[1].min()}')
print(f'Total marks of second student is {marks_arr[1].sum()}')
print(f'Average marks of second student is {marks_arr[1].mean()}')
pass_chanceofsecondstudent = 0
for mark in marks_arr[1]:
  if mark >= 30:
    pass_chanceofsecondstudent += 1

#analysis of third student
print(f'Highest marks of third student is {marks_arr[2].max()}')
print(f'Lowest marks of third student is {marks_arr[2].min()}')
print(f'Total marks of third student is {marks_arr[2].sum()}')
print(f'Average marks of third student is {marks_arr[2].mean()}')
pass_chanceofthirdstudent = 0
for mark in marks_arr[2]:
  if mark >= 30:
    pass_chanceofthirdstudent += 1

#analysis of fourth student
print(f'Highest marks of fourth student is {marks_arr[3].max()}')
print(f'Lowest marks of fourth student is {marks_arr[3].min()}')
print(f'Total marks of fourth student is {marks_arr[3].sum()}')
print(f'Average marks of fourth student is {marks_arr[3].mean()}')
pass_chanceoffourthstudent = 0
for mark in marks_arr[3]:
  if mark >= 30:
    pass_chanceoffourthstudent += 1

#analysis of fifth student
print(f'Highest marks of fifth student is {marks_arr[4].max()}')
print(f'Lowest marks of fifth student is {marks_arr[4].min()}')
print(f'Total marks of fifth student is {marks_arr[4].sum()}')
print(f'Average marks of fifth student is {marks_arr[4].mean()}')
pass_chanceoffifthstudent = 0
for mark in marks_arr[4]:
  if mark >= 30:
    pass_chanceoffifthstudent += 1

# who has the highest average marks amongst the students?
avg_list = list()
for i in marks_arr:
  i = i.mean()
  avg_list.append(i)
max_avg = avg_list[0]
for i in avg_list:
  if i > max_avg:
    max_avg = i
print(f'The highest average in class is {max_avg}')


#subject wise analysis

# average score in first subject
first_column = marks_arr[:, 0]
print(f'average of the first subject is {first_column.mean()}')

# average score in second subject
second_column = marks_arr[:, 1]
print(f'average of the second subject is {second_column.mean()}')

# average score in third subject
third_column = marks_arr[:, 2]
print(f'average of the third subject is {third_column.mean()}')

# easiest and most difficult subject as per average scored

subject_avgs = {first_column.mean(), second_column.mean(), third_column.mean()}
lowest_avg_sub = min(subject_avgs)
highest_avg_sub = max(subject_avgs)
print(f'Subject-wise highest average was {highest_avg_sub} and lowest average was {lowest_avg_sub}')


# did the student pass the overall exam?
if pass_chanceoffirststudent == 3:
  print('first student passed')
else:
  print('first student failed')

if pass_chanceofsecondstudent == 3:
  print('second student passed')
else:
  print('second student failed')

if pass_chanceofthirdstudent == 3:
  print('third student passed')
else:
  print('third student failed')

if pass_chanceoffourthstudent == 3:
  print('fourth student passed')
else:
  print('fourth student failed')

if pass_chanceoffifthstudent == 3:
  print('fifth student passed')
else:
  print('fifth student failed')