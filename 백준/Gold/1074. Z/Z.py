import sys

input_value = sys.stdin.read().split()

rows = 2 ** int(input_value[0]) 
cols = 2 ** int(input_value[0])

count = 0
result = 0

coordinate = {}

def main():
    fill(0, 0, 2 ** int(input_value[0]))

def fill(rows, cols, size):
    global count
    global result
    global coordinate
        
    r, c = int(input_value[1]), int(input_value[2])
    if (r, c) in coordinate:
        print(coordinate[(r, c)])
        

    if size == 2:
        coordinate[(rows, cols)]       = count; count += 1
        coordinate[(rows, cols + 1)]   = count; count += 1
        coordinate[(rows + 1, cols)]   = count; count += 1
        coordinate[(rows + 1, cols + 1)] = count; count += 1
        
        if rows <= r < rows + 2 and cols <= c < cols + 2:
            print(coordinate[(r, c)])
            sys.exit(0)
        return
    
    half = size // 2
    
    block = half * half

    # (r,c)가 속한 사분면만 들어가도록 조건 분기
    if r < rows+half and c < cols+half:           # 좌상
        fill(rows, cols, half)
    elif r < rows+half and c >= cols+half:        # 우상
        # 좌상 크기만큼 count 미리 증가
        count += block
        fill(rows, cols+half, half)
    elif r >= rows+half and c < cols+half:        # 좌하
        count += 2*block
        fill(rows+half, cols, half)
    else:                                         # 우하
        count += 3*block
        fill(rows+half, cols+half, half)


if __name__ == "__main__" :
    main()
    

