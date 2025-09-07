import sys
import itertools

input_value = sys.stdin.read().splitlines()
tmp = [int(x) for x in input_value]

temp_arr = itertools.permutations(tmp, 7)

result = []

for i in temp_arr:

    if sum(i) == 100:
        result = sorted(i)
        break

for i in range(0, len(result)):
    print(result[i])