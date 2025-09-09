import sys

sys.setrecursionlimit(1_000_000) 

rd = sys.stdin.read().splitlines

input_value = rd()
todo_arr = int(input_value.pop(0))
input_value = list(map(int, input_value))

def sort(arr):
    if int(len(arr)) <= 1:
        return arr
    
    pivot = arr[len(arr) // 2]
    right = []
    left = []
    mid = []
    
    for i in range(0, len(arr)):
        if arr[i] < pivot:
            left.append(arr[i])
        elif arr[i] > pivot:
            right.append(arr[i])
        else:
            mid.append(arr[i])
    
    if len(left) != 1:
        left = sort(left)
    
    if len(right) != 1:
        right = sort(right)
        
    return left + mid + right
        
    
def main():
    if len(input_value) > 100000:                
        input_value.sort()
        sys.stdout.write("\n".join(map(str, input_value)))
    else:                                         
        res = sort(input_value)
        sys.stdout.write("\n".join(map(str, res)))
    
if __name__ == "__main__" :
    main()
    
    

