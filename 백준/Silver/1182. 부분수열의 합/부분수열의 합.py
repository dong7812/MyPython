import sys
import itertools

input_value = sys.stdin.read().splitlines()

N, A = (input_value[0]).split()
elements = [int(x) for x in (input_value[1]).split()]

# 부분 수열이 될 수 있는 최대 숫자
MAX = 2 ** int(N) - 1

count = 0

def sum_elements(result, arr):
    global count
    
    arr = list(map(int, arr))
    for i in range(int(N)):
        for p in itertools.combinations(arr, i+1) :
            if len(p) != 0:
                temp = sum(p)
                if temp == int(result) :
                    count += 1 
    return count        

print(sum_elements(A, elements))