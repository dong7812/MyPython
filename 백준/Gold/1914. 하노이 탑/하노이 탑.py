count = 0
num = 0

def main():
    input_value = int(input())
    global num
    num = input_value
    print(2**input_value - 1)
    if(num <= 20):
        hanoi(input_value, 1, 3, 2)
    
    

def move(n, start, to):
    global count
    count += 1
    if(num <= 20):
        print(start, to)
    
def hanoi(n, from_tower, to_tower, tem_tower):
    if n <= 1:
        move(n, from_tower, to_tower)
        return 1
    else :
        hanoi(n-1, from_tower, tem_tower, to_tower)
        move(n, from_tower, to_tower)
        hanoi(n-1, tem_tower, to_tower, from_tower)
        return 
    
if __name__ == "__main__":
    main()
    