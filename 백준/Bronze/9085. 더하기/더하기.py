T = int(input())
total = 0

for t in range(1, T+1):
    N = int(input())
    numbers = sum(list(map(int, input().split())))
    
    print(numbers)