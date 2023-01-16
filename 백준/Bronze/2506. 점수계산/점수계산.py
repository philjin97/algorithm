N = int(input())
numbers = list(map(int, input().split()))
cnt = 0
result = 0

for n in numbers:
    if n == 1:
        result += 1 + cnt
        cnt += 1
    else:
        cnt = 0

print(result)
