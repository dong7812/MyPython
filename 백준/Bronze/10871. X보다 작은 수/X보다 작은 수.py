import sys

input_value = sys.stdin.read().splitlines()

len_arr, *find = [int(x) for x in input_value[0].split()]

arr = [int(x) for x in input_value[1].split()]

result = ""

for i in range(0, len_arr):
    if arr[i] < find[0]:
        result += str(arr[i])+ " "
        
print(result)