input_value = int(input())

col_used = [False] * input_value

idx1_used = [False] * (input_value * 2 - 1)
idx2_used = [False] * (input_value * 2 - 1)

count = 0

def main():
    nQueen(0)
    print(count)

def nQueen(row):
    global count
    if row == input_value:
        count += 1
    
    for col in range(0, input_value):
        idx1 = row + col
        idx2 = row - col + (input_value - 1)
        if not col_used[col] and not idx1_used[idx1] and not idx2_used[idx2]:
            col_used[col] = idx1_used[idx1] = idx2_used[idx2] = True
            nQueen(row+1)
            col_used[col] = idx1_used[idx1] = idx2_used[idx2] = False

if __name__ == "__main__":
    main()