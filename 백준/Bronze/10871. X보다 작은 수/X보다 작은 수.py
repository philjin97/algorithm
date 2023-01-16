(a, b) = list(map(int, input().split(' ')))
number = list(map(int, input().split(' ')))

for each in range(a):
    if number[each] < b:
        print(number[each], end=' ')
    