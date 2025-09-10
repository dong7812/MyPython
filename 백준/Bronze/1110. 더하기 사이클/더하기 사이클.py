import sys

N = int(sys.stdin.read())

count = 0

def plus(num, target):
    global count
    
    count += 1
    
    if target == 0:
        return count
    
    arr = [int(x) for x in list(str(num).zfill(2))] 
    result = arr[1] * 10 + (arr[0] + arr[1]) % 10
    
    if result == target:
        return count
    else:
        return plus(result, target)

print(plus(N, N)) 