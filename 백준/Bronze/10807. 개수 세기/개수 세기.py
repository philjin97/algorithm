n = int(input())
numbers = list(map(int, input().split()))
v = int(input())
count = 0

for a in range(n):
    if numbers[a] == v:
        count += 1

print(count)