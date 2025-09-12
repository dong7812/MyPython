import sys

input_value = sys.stdin.read().splitlines()

result = []

for i in input_value[1:] :
    if int(i) != 0:
        result.append(i)
    elif int(i) == 0:
        result.pop()
        
print(sum(int(x) for x in result))