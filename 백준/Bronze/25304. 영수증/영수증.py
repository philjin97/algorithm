total = int(input())
n = int(input())
real_total = 0

for a in range(1, n+1):
    (a, b) = list(map(int, input().split()))
    real_total += a * b

if total == real_total:
    print('Yes')
else:
    print('No')
