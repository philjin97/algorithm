n = int(input())
line = []

for num in range(n):
    line.append(input())

line = list(set(line))
line.sort()
line.sort(key=lambda x:len(x))

print('\n'.join(line))