import math

input_value = input()

up = input_value.split()[0]
down = input_value.split()[1]
h = input_value.split()[2]

# 초기 세팅
need = int(h) - int(up)
daygo = int(up) - int(down)

if int(h) <= int(up):
    print(1)
else:
    temp = math.ceil((int(h) - int(up)) / daygo + 1)
    print(temp)