# To do list
print('---- Welcome to To Do List ----')

# Creating a list
tasks = []
print('\n1.Add Task \n2.Delete Task \n3.Display Tasks \n4.Exit')

# loop for adding, deleting and displaying tasks
while True:
    choice = int(input('Enter your choice: '))
    match(choice):
        case 1:
            taska = input('Enter task: ')
            tasks.append(taska)
            print('\n task added succesfully')
            print(tasks)
            continue
        case 2:
            taskd = input('Enter the task you want to delete: ')
            print(tasks)
            tasks.remove(taskd)
            print(tasks)
            continue
        case 3:
            print('To Do List')
            print(tasks)
            continue
        case 4: 
            print('Exiting')
            break
        case _: 
            print('Invalid input')
