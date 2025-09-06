import sys

input_value = sys.stdin.read().splitlines()

paper = input_value[0]
row = [0]
height = [0]

for i in range(2, len(input_value)):
    # 커팅 위치 파악하기 (가로 0, 세로 1)
    a = input_value[i].split()[0]
    b = input_value[i].split()[1]
    if int(a) == 0:
        height.append(int(b))
    else:
        row.append(int(b))
        
row.append(int(paper.split()[0]))
height.append(int(paper.split()[1]))

height_diff = [b - a for a, b in zip(sorted(row)[:-1], sorted(row)[1:])]
row_diff = [b - a for a, b in zip(sorted(height)[:-1], sorted(height)[1:])]

print(max(row_diff) * max(height_diff))