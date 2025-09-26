import sys

input_value = sys.stdin.read().splitlines()

limit = int(input_value[0])

count = 0
temp = []

def finb(num, arr, goal):
    dp = [0] * (goal + 1)
    
    dp[0] = 1

    for coin in arr:
        for j in range(coin, goal+1):
            dp[j] += dp[j-coin]            
    return dp[goal]

for i in input_value[1:]:
    count += 1
    temp.append(i)    
    if count == 3:
        num = int(temp[0])
        arr = [int(x) for x in temp[1].split()]
        goal = int(temp[2])
        
        print(finb(num, arr, goal))
        
        temp = []
        count = 0
        


