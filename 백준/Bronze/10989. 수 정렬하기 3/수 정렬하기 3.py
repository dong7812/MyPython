import sys

input_value = sys.stdin.buffer.readline  

write = sys.stdout.buffer.write

MAX = 10000
counting = [0] * (MAX + 1)               

N = int(input_value())                   
for _ in range(N):                      
    x = int(input_value())
    counting[x] += 1  
    
for i in range(0, MAX+1):
    c = counting[i]
    if c:
        for _ in range(c):
            print(i)
