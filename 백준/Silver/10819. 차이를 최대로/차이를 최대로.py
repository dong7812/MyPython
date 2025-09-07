import sys
import itertools

input_value = sys.stdin.read().splitlines()

def do_add():
    tmp = [int(x) for x in input_value[1].split()]
    
    temp_arr = list(itertools.permutations(tmp, int(input_value[0])))
    compare_arr = []
    for i in temp_arr:
        tmp_add = []
        for j in range(0, int(input_value[0])-1):
            tmp_add.append(sum_idx(i, j))
        compare_arr.append(sum(tmp_add))  
    
    print(max(compare_arr))  

def main():
    do_add()

def sum_idx(arr, idx):
    return abs(arr[idx] - arr[idx+1])

if __name__ == "__main__" :
    main()