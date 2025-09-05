import sys

input_value = sys.stdin.read().splitlines()

for i in range(1, int(input_value[0])+1):
    x = 0
    arr = input_value[i].split("X")

    for i in range(0, len(arr)):
        x += sum(range(1, len(arr[i])+1))
        
    print(x)