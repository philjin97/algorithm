total = 0
small = 0

for t in range(7):
    num = int(input())
    if num % 2 == 1:
        total += num
        if small == 0:
            small = num
        elif small > num:
            small = num

if total == 0:
    print(-1)
else: 
    print(total, small, sep='\n')