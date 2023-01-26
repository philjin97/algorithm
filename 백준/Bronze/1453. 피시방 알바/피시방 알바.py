N = int(input())
seat = list(map(int, input().split()))
computer = []
cnt = 0

for n in range(N):
    if seat[n] in computer:
        cnt += 1
    else:
        computer.append(seat[n])

print(cnt)