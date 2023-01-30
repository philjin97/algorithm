position = [list(map(int, input().split())) for _ in range(4)]
rec = []

for a in range(4):
    for n in range(position[a][0], position[a][2]):
        for i in range(position[a][1], position[a][3]):
            if (str(n) + str(i)) not in rec:
                rec.append(str(n) + str(i))

print(len(rec))