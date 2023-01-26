k = int(input())
total = []

for n in range(k):
    price = int(input())
    if price != 0:
        total.append(price)
    else:
        total.pop()

print(sum(total))
    