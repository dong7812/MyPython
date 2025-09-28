import sys, re

input_value = sys.stdin.read()

p_idx = []

# 묶음으로 나오게 
tokens = re.findall(r'\d+|[+-]', input_value)

i = 0
while i < len(tokens):
    if tokens[i] == '+':
        s = int(tokens[i-1]) + int(tokens[i+1])
        tokens[i-1:i+2] = [str(s)]
        i = max(0, i-1)  # 바로 앞에서 다시 검사 (스킵 방지)
    else:
        i += 1
                
expr = ''.join(tokens)
# 핵심: 모든 '숫자 덩어리'를 int로 한번 변환해 선행 0 제거
expr_norm = re.sub(r'\d+', lambda m: str(int(m.group(0))), expr)

print (eval(expr_norm))
