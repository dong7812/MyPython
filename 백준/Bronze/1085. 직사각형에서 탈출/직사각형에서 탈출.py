x, y, w, h = map(int, input().split())

result = min((w-x), x, (h-y), y)
print(result)