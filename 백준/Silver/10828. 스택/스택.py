import sys

input_value = sys.stdin.read().splitlines()

result = []

for i in input_value :
    if "push" in i :
        result.append((i.split())[1])
    elif "pop" in i :
        if len(result) != 0:
            print(result[len(result)-1])
            result.pop(len(result)-1)
        else:
            print(-1)
    elif "top" in i:
        if len(result) != 0:
            print(result[len(result)-1])
        else:
            print(-1)
    elif "size" in i:
        print(len(result))
    elif "empty" in i:
        if len(result) == 0:
            print(1)
        else:
            print(0)
            