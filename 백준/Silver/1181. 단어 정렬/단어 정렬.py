import sys

input_value = sys.stdin.read().splitlines()

tmep_dict = {}

for i in range(1, len(input_value)):
    tmep_dict[str(input_value[i])] = len(input_value[i])

d1 = sorted(tmep_dict.items(), key=lambda x: (x[1] , x[0]))

for word, _ in d1:
    print(word)
