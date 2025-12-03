class AgeError(Exception):
    pass  

def get_age():
    age = int(input('Enter age: '))
    if age < 0:
        raise AgeError("Age can't be negative")
    else:
        return age

try:
    print(get_age())
except AgeError as e:
    print(e)
