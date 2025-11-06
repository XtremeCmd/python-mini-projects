stack = []

def push(item):
  stack.append(item)

def pop():
  if stack:
    print(stack.pop())
  else:
    print('Stack is empty!!')
    
def peek():
    if not stack:
        print('Stack is empty!!')
    else:
        print(stack[0])
        
def isEmpty():
    if not stack:
        print('Stack is empty')
    else:
        print('Stack is not empty')
    
def size():
    print(len(stack))

push(20)
push(10)
print(stack)
pop()
print(stack)
isEmpty()
size()
pop()
print(stack)
isEmpty()