import sys

input_value = sys.stdin.read().splitlines()

for i in range (1, len(input_value)):
    count = 0
    tmp = input_value[i].split(" ")
    score_arr = [int(x) for x in tmp]
    # 각 줄 평균
    average = (sum(score_arr)-score_arr[0]) // score_arr[0]
    
    for j in range(1, score_arr[0] + 1):
        if(average < score_arr[j]):
            count += 1
    
    arr_result = count / score_arr[0] * 100.000      
    print("%.3f%%" %round(arr_result, 3))