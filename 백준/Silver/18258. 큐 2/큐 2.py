import sys
from collections import deque

input_value = sys.stdin.read().splitlines()

N, *arr = input_value

class Queue:
    
    def __init__(self):
        self.items = deque()
        
    def enqueue(self, item):
        self.items.append(item)
        
    def dequeue(self):
        if not self.is_empty():
            return self.items.popleft()
        return None

    def is_empty(self):
        return len(self.items) == 0
    
queue = Queue()

for i in arr:
    if "push" in i:
        queue.enqueue(i.split()[1])
    elif "pop" in i:
        if queue.is_empty():
            print(-1)
        else:
            print(queue.items[0])
            queue.dequeue()
    elif "front" in i:
        if queue.is_empty():
            print(-1)
        else:
            print(queue.items[0])        
    elif "back" in i:
        if queue.is_empty():
            print(-1)
        else:
            print(queue.items[len(queue.items)-1])
    elif "empty"in i:
        if queue.is_empty():
            print(1)
        else:
            print(0)
    elif "size" in i:
        print(len(queue.items))
    
    
