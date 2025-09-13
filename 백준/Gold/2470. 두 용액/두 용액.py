import sys

input_value = sys.stdin.read().splitlines()

(first, *rest) = input_value

N = int(first)
_arr = sorted(list(map(int, rest[0].split())))

def divide(arr, left = 0, right = 0):
    
    #  초기 값 지정 
    if left == 0 and right == 0:
        left , right = 0, N-1
        
    best = abs(arr[left] + arr[right])
    best_l, best_r = left, right
    
    while left < right:
        sum_arr = arr[left] + arr[right]   
        
        if best > abs(sum_arr):
            best = abs(sum_arr)
            best_l, best_r = left, right
            
            if best == 0:
                break
            
        if sum_arr > 0:
            right -= 1
        else:  
            left += 1
                
    return best_l, best_r


result = divide(_arr)
print(_arr[result[0]], _arr[result[1]])