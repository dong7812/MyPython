import sys
import math

input_value = sys.stdin.read().split()

S = int(input_value[0])
T = int(input_value[1])

isPrime = [True] * (T+1)
show_prime = []

def find(_from, _to):
    for i in range(2, int(_to**0.5)+1):
        if isPrime[i] :
            for j in range(i*i, _to+1, i):
                isPrime[j] = False
    
    for i in range(0, len(isPrime)):
        if isPrime[i] and i >= _from and i != 0 and i != 1:
            show_prime.append(i)
            
    for i in show_prime:
        print(i)    
    
def main():
    find(S, T)
    
if __name__ == "__main__" :
    main()