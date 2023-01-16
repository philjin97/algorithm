numbers = list(map(int, input().split()))
dice = {}

for num in numbers:
    if num in dice:
        dice[num] += 1
    else:
        dice[num] = 1

if len(dice) == 1:
    print(10000 + (num * 1000))
elif len(dice) == 2:
    for key in dice:
        if dice[key] == 2:
            print(1000 + (key * 100))
else: 
    keyss = sorted(list(dice), reverse=True)
    print(keyss[0] * 100) 