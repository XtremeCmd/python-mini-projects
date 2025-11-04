def calculator():
    op = input('Enter what operation you want to do: +, -, *, /')
    a = float(input('Enter the first number: '))
    b = float(input('Enter the second number: '))

    if op == '+':
        result =  a + b
    elif op == '-':
        result =  a - b
    elif op == '*':
        result = a * b
    elif op == '/':
        result = a / b if b != 0 else print('Error can\'t divide with zero')
    else:
        result = 'Invalid operation'

    print('Result: ', result)

    again = input('Do you want to do another calculation?: (y/n)')
    if again.lower() == 'y':
        calculator() 

calculator()  