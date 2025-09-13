import sys
from collections import deque

input_value = sys.stdin.read()

N = int(input_value)

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

for i in range(1, N+1):
    queue.enqueue(i)
    
while len(queue.items) >= 1:
    
    if(len(queue.items) == 1):
        break
    
    queue.dequeue()
    
    queue.enqueue(queue.items[0])
    queue.dequeue()
    

print(queue.items[0])
