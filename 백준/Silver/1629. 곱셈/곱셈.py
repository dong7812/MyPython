import sys

a,b,c= sys.stdin.read().split()

def modular_exponentiation(a, b, c):
    result = 1
    a = a % c 
    while b > 0:
        if b % 2 == 1:
            result = (result * a) % c
        a = (a * a) % c 
        b //= 2 
    return result

print(modular_exponentiation(int(a), int(b), int(c)))
