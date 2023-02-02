n = int(input())
graph = [[0] for _ in range(3)]
graph[0][0] = 1

for _ in range(n):
    v1, v2 = list(map(int, input().split()))
    if graph[v1 -1][0] == 1:
        graph[v1 -1][0] = 0
        graph[v2 -1][0] = 1
    elif graph[v2 -1][0] == 1:
        graph[v2 -1][0] = 0
        graph[v1 -1][0] = 1
    else:
        continue

for a in range(3):
    if graph[a][0] == 1:
        print(a + 1)