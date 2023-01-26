n = int(input())
original = []
trash = []

for num in range(n):
    original.append(num+1)

for num in range(n):
    if len(original) > 1:
        trash.append(original.pop(0))
        original.append(original.pop(0))
    else:
        break

for a in trash:
    print(a, end=' ')
print(original[0])