import sys

input = sys.stdin.read().splitlines()

N, *temp = input

arr = [int(x) for x in temp[0].split()]

time_arr = [0] * int(N)

_sum = 0

for i in range(int(N)):
    _sum += sorted(arr)[i]
    time_arr[i] = _sum
    
print(sum(time_arr))