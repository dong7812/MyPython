import sys

input_value = sys.stdin.read()

N, M = input_value.split()

class Queue:
    rear = 0
    front = 0
    MAX_SIZE = int(N) + 1
    queue = list()
    def __init__(self):
        self.rear = 0
        self.front = 0
        self.queue = [None for i in range(self.MAX_SIZE)]
        
    def enqueue(self, item):
        if not self.isFull():
            self.rear = (self.rear+1) % self.MAX_SIZE
            self.queue[self.rear] = item
        
    def dequeue(self):
        if not self.is_empty():
            self.front = (self.front+1) % self.MAX_SIZE
            val = self.queue[self.front]
            self.queue[self.front] = None   # 선택: 시각적 정리
            return val
        return None
    
    def peek(self):
        if not self.is_empty():
            return self.queue[(self.front+1) % self.MAX_SIZE]

    def is_empty(self):
        if self.front == self.rear:
            return True
        return False
    
    def isFull(self):
        return self.front == (self.rear+1) % self.MAX_SIZE
    
    def clear(self):
        self.front = self.rear

circular_queue = Queue()
test = []
for i in range(1, int(N)+1):
    test.append(i)
    circular_queue.enqueue(i)
    
res = []
while not circular_queue.is_empty():
    for _ in range(int(M) - 1):
        circular_queue.enqueue(circular_queue.dequeue())  # 맨 앞을 뒤로
    res.append(circular_queue.dequeue())                  # M번째 제거
    
print("<" + ", ".join(map(str, res)) + ">")