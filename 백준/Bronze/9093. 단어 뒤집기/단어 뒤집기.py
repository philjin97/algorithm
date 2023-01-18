T = int(input())

for t in range(1, T+1):
    words = input().split()
    for w in words:
        rev_w = w[::-1]
        print(rev_w, end=' ')