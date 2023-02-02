n = int(input())
mapping = list(map(int, input().split()))
up = []
current_up = 0

for a in range(n-1):
        if mapping[a + 1] > mapping[a]:
            if a + 1 == n - 1:
                current_up += mapping[a + 1] - mapping[a]
                up.append(current_up)
            else:
                current_up += mapping[a + 1] - mapping[a]
        else:
            up.append(current_up)
            current_up = 0

up = sorted(up)

print(up[-1])