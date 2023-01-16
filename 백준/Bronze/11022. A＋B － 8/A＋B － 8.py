T = int(input())

for t in range(1, T+1):
    (a, b) = list(map(int, input().split(' ')))
    print(f'Case #{t}: {a} + {b} = {a + b}')