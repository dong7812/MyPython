import sys

input_value = sys.stdin.read().splitlines()

N, *arr = map(int,input_value)

max_hi = 0

count = 0

for i in reversed(arr):
     if i > max_hi:
        count += 1
        max_hi = i

print(count)
