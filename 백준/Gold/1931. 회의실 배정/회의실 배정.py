import sys

input_value = sys.stdin.read().splitlines()

N = int(input_value[0])

arr = []

for i in sorted(input_value[1:]):
    arr.append(list(map(int, i.split())))
  
arr.sort(key=lambda x: x[1])

cnt, temp = 0, 0
for s, e in arr:
    if s >= temp:
        cnt += 1
        temp = e
        
print(cnt)