k = int(input())
total = []
 
for n in range(k):
    num = int(input())
    if num == 0:
        total.pop()
    else:
        total.append(num)

print(sum(total))