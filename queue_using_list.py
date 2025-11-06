queue = []

def enQueue(item):
    queue.append(item)
    
def deQueue():
    if not queue:
        print('Queue is empty, can\'t dequeue')
    else:
        queue.pop(0)

def front():
    if not queue:
        print('Queue is empty')
    else:
        print(queue[0])
        
def isEmpty():
    if not queue:
        print('Queue is empty')
    else:
        print('Queue is not empty')
        
def size():
    print(len(queue))
    
enQueue(2)
enQueue(3)
print(queue)
deQueue()
print(queue)
isEmpty()
size()