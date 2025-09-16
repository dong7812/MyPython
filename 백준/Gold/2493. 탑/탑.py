import sys

N, *arr = sys.stdin.read().splitlines()

input_arr = [int (x) for x in arr[0].split()]

t = []
temp_arr = []
seperator = " "
def find_idx(arr):
    global t
    global temp_arr
    n = int(N)
    
    # 다음 인덱스를 갖고 있기
    prev_pos = [i - 1 for i in range(n)]

    # 각 위치 i에 대해, 왼쪽에서 처음 큰 값의 인덱스를 찾음
    for i in range(n):
        j = prev_pos[i]        # 바로 왼쪽부터 시작
        chain = []             # 경로 압축용 기록

        while j != -1 and arr[j] <= arr[i]:
            chain.append(j)
            j = prev_pos[j]

        for k in chain:
            prev_pos[k] = j

        t.append(j if j != -1 else -1)

    for idx in t:
        if idx == -1:
            temp_arr.append(0)
        else:
            temp_arr.append(idx + 1)
    result = seperator.join([str(num) for num in temp_arr])
    return result

print(find_idx(input_arr))