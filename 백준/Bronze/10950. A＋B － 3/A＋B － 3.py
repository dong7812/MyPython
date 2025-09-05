import sys

arr = sys.stdin.read().splitlines()

n = int(arr[0])   
for i in range(1, n + 1):
    a, b = map(int, arr[i].split())
    print(a + b)