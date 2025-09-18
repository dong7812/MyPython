import sys

input_value = sys.stdin.read().splitlines()

N, N_arr, M, M_arr = input_value

first_arr = [int(x) for x in N_arr.split()]
second_arr = [int(x) for x in M_arr.split()]

first_dict  = {}
result_stack = []

for i in first_arr:
    first_dict[i] = True

def find(arr):
    for i in arr:
        if first_dict.get(i) :
            result_stack.append(1)
        else:
            result_stack.append(0)
    return " ".join(map(str, result_stack))

print(find(second_arr))