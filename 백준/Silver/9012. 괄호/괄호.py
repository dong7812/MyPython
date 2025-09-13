import sys

input_value = sys.stdin.read().splitlines()

N, *arr = input_value

for i in arr:
    temp = list(i)
    _find = []
    broken = False  # 루프 전
    
    for j in temp:
        if j == "(":
            _find.append(True)
        elif j == ")":
            if len(_find) == 0:
                print("NO")
                broken = True
                break
            else :
                _find.pop()       
        
    if not broken:
        if len(_find) == 0 : 
            print("YES")
        else:
            print("NO")
  
    