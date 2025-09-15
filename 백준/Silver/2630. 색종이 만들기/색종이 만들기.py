import sys

input_value = sys.stdin.read().splitlines()

N, *arr = input_value

new_arr = []

rows = int(N) 
cols = int(N)

# 일단 색 하나만 세기
count = 0
count_2 = 0
result = 0

for i in arr:
    temp = i.split()
    new_arr.append(temp)
  
def find(arr, r, c, n):
    global count, count_2

    first = arr[r][c]
    same = True

    for i in range(r, r+n):
        for j in range(c, c+n):
            if arr[i][j] != first:
                same = False
                break
        if not same:
            break

    if same:  # 블록 전체가 같은 색일 때만 카운트
        if first == "0":
            count += 1
        else:
            count_2 += 1
        return

    # 더 쪼갤 수 없으면 종료
    if n == 1:
        return

    half = n // 2
    find(arr, r, c, half)           # 1사분면
    find(arr, r, c+half, half)      # 2사분면
    find(arr, r+half, c, half)      # 3사분면
    find(arr, r+half, c+half, half) # 4사분면
    
    return count, count_2

result = find(new_arr, 0, 0, int(N))

print(count)
print(count_2)
    
      
