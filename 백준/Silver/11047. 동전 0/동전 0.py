import sys

input_value = sys.stdin.read().splitlines()

N, M = map(int, input_value[0].split())

arr = [int(x) for x in input_value[1:]]

count = 0
def divide(m):
    global count
    t = [m] 
    temp = [int(x) for x in arr if x <= m]
    
    if len(temp) == 0:
        return 0
    
    for i in reversed(temp):
        kk = t.pop()
        if kk >= 0:
            count += kk // i
            t.append(kk%i)
        else:
            return 0
    return count

print(divide(M))