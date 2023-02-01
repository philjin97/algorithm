(n, m) = list(map(int, input().split()))
cards = list(map(int, input().split()))
max_sum = 0

for a in cards:
    for b in cards:
        for c in cards:
            if a != b and b != c and a != c:
                if a + b + c <= m and a + b + c > max_sum:
                    max_sum = a + b + c
                    

print(max_sum)