n = 0
result = 0

while n < 5:
    a = int(input())
    if a < 40:
        a = 40
    result += a
    n += 1

print(result // 5) 