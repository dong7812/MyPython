import sys

input_value = sys.stdin.read().splitlines()

s, target = input_value
stack = []


for i in s:
    stack.append(i)
    if "".join(stack[-len(target):]) == target:
        for j in range(len(target)):
            stack.pop()

result = "".join(stack)

if result == "":
    print("FRULA")
else:
    print(result)