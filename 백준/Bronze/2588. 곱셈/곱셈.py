s = [input() for _ in range(2)]

a = int(s[0]) * int(list(s[1])[2])
b = int(s[0]) * int(list(s[1])[1])
c = int(s[0]) * int(list(s[1])[0])
print(a)
print(b)
print(c)
print(a + b*10 + c*100)
