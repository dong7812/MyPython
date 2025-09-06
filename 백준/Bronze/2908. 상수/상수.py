input = input()

arr = input.split()

a = arr[0][::-1]
b = arr[1][::-1]

if int(a) > int(b):
    print(a)
else:
    print(b)