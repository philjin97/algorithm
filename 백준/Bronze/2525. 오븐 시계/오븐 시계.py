(a, b) = list(map(int, input().split()))
time = int(input())

a += (b + time) // 60
b = (b + time) % 60

if a >= 24:
    a -= 24

print(a, b, sep=' ')
