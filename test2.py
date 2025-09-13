input_value = int(input())

# 같은 행 사용여부
col_used = [False] * input_value
# 상단 대각선 이용여부
up_dialog_used = [False] * (input_value * 2 -1)
# 하단 대각선 이용 여부
down_dialog_used = [False] * (input_value * 2 -1)
count = 0

def main():
    nQueen(0)
    print(count)

def nQueen(row):
    global count
    if row == input_value:
        count += 1
        return    
    for i in range(0, input_value):
        # 상단 대각선 index 증가
        idex_up = row + i
        # 하단 대각 선 index 하락 (음수 보정을 위한 오프셋으로 input-1)
        idex_down = row - i + (input_value - 1)
        
        if not col_used[i] and not up_dialog_used[idex_up] and not down_dialog_used[idex_down]:
            col_used[i] = up_dialog_used[idex_up] = down_dialog_used[idex_down] = True
            nQueen(row + 1)
            col_used[i] = up_dialog_used[idex_up] = down_dialog_used[idex_down] = False

if __name__ == "__main__":
    main()
