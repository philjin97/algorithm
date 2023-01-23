numbers = []
max = [0, 0]

for a in range(9):
    numbers.append(int(input()))
    if numbers[a] > max[0]:
        max[0] = numbers[a]
        max[1] = a + 1

print(max[0], max[1], sep='\n')