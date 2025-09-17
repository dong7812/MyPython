import sys

s = list(sys.stdin.read())

def find_sum(s):
    type_check = []  # 여는 괄호 검증용 스택: '(', '['만 저장
    sum_check  = []  # 각 깊이의 누적 합 스택: 여는 괄호마다 0을 push

    for ch in s:
        if ch not in '()[]':  # 공백/개행 등은 무시
            continue

        if ch == '(':
            type_check.append('(')
            sum_check.append(0)             # 이 괄호 내부 합을 쌓을 바구니
        elif ch == '[':
            type_check.append('[')
            sum_check.append(0)
        elif ch == ')':
            # 짝 검증
            if not type_check or type_check[-1] != '(':
                return 0
            type_check.pop()

            inner = sum_check.pop()         # 이 괄호 내부 합
            val = 2 if inner == 0 else 2*inner

            if sum_check:                   # 상위 깊이에 더하기
                sum_check[-1] += val
            else:                           # 최상위면 새로 담기
                sum_check.append(val)
        else:  # ch == ']'
            if not type_check or type_check[-1] != '[':
                return 0
            type_check.pop()

            inner = sum_check.pop()
            val = 3 if inner == 0 else 3*inner

            if sum_check:
                sum_check[-1] += val
            else:
                sum_check.append(val)

    # 모든 괄호가 닫혔는지 확인
    if type_check:
        return 0

    # sum_check에는 최상위 합(또는 부분 합들)이 남아 있음 → 전부 더하기
    return sum(sum_check) if sum_check else 0

print(find_sum(s))