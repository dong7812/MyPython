import sys

input_value = sys.stdin.read().splitlines()

tmp_list = [int(x) for x in input_value]

result = 1

for i in tmp_list:
    result *= i

for i in range(0, 10):
    recur = str(result).count(str(i))
    print(recur)
    