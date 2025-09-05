import sys

def checkPrime(h):
    # 0부터 h까지
    isPrime = [True] * (h + 1)
    isPrime[0] = isPrime[1] = False
    
# h까지의 수중 최대 배수는 제곱근 근사치가 된다.
    for i in range(2, int(h**0.5) + 1): 
        if isPrime[i]:
            # i의 배수들을 h+1까지 i의 배수씩 선회
            for j in range(i*i, h+1, i):
                isPrime[j] = False

    # 범위내 최대 소수
    maxIndex = max(filter(lambda i: isPrime[i], range(h+1)))
    
    return isPrime

def goldbach(n):
    isPrime = checkPrime(n)
    
    # 단순 n - 소수의 결과가 소수가 아닌 경우도 존재 그렇기에 하나씩 뒤로 돌리면서 확인
    for i in range(n//2, 1, -1):
        if isPrime[i] and isPrime[n-i]:
            return i, n-i
    return None

def main():
    input = sys.stdin.readline
    while True:
        line = input()
        if not line:
            break
        n = int(line)
        if n == 0:
            break
        
        result = goldbach(n)
        if result is not None :
            a, b = result
            print(a ,b)
            
if __name__ == "__main__":
    main()