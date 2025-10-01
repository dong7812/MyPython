import sys

input_value = sys.stdin.read().splitlines()

N = int(input_value[0])

first_arr = list(map(int, input_value[1].split()))
second_arr = list(map(int, input_value[2].split()))

indexed_second = [(second_arr[i], i) for i in range(N)]
indexed_second.sort(reverse=True)

sorted_first = sorted(first_arr)

new_arr = [0] * N
temp = 0

for rank, (value, original_idx) in enumerate(indexed_second):
    new_arr[original_idx] = sorted_first[rank]

for i in range(N):
    temp += new_arr[i] * second_arr[i]

print(temp)
