from sys import stdin

n = int(stdin.readline())
t_input = int(n ** 0.5) + 1

for i in range(2, t_input):
    while n % i == 0:
        print(i)
        n //= i

if n > 1:
    print(n)
    print("\n")