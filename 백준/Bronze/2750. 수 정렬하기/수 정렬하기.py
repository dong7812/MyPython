import sys

input_value = sys.stdin.read().splitlines()

int_arr = [int(x) for x in input_value]

int_arr.pop(0)

result = sorted(set(int_arr))

for i in range(0, len(result)):
    print(result[i])