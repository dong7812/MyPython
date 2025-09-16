import sys

input_value = sys.stdin.read().splitlines()

N, *arr = input_value

temp = [int (x) for x in list(arr)[0].split()]

def find_idx(arr, target):
    start, end = 0, len(arr)   
    while start < end:
        mid = (start + end) // 2
        if arr[mid] >= target:     
            end = mid
        else:
            start = mid + 1
    return start

a = []
for i in temp:
    pos = find_idx(a, i) 
    if pos == len(a):
        a.append(i)  
    else:
        a[pos] = i

print(len(a))