input_value = int(input())
count = 0

if (input_value < 100):
    print(input_value)
else:
    for i in range(100, input_value+1):
        arr = [int(x) for x in list(str(i))]
        if arr[2] - arr[1] == 0 and arr[1] - arr[0] == 0:
            count += 1
        elif (arr[2] - arr[1]) == (arr[1] - arr[0]):
            count += 1
        elif (arr[2] - arr[1]) == 0 and arr[1] - arr[0] != 0:
            count += 0
        elif (arr[2] - arr[1]) != 0 and arr[1] - arr[0] == 0:
            count += 0
        else:
            count += 0       
    print(count + 99)