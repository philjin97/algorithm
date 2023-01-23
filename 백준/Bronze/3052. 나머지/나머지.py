numbers = []
remainder = {}

for n in range(10):
    numbers.append(int(input()))

for a in numbers:
    remainder[a % 42] = 0

print(len(list(remainder)))