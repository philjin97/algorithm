total = []

for a in range(1, 31):
    total.append(a)

for n in range(28):
    hw = int(input())
    total.remove(hw)

for missing in total:
    print(missing)