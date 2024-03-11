import sys
input = sys.stdin.readline
from collections import deque

dx = [0,1,0,-1]
dy = [1,0,-1,0]
n,m = map(int, input().split())
graph = [[0] * m for _ in range(n)]
visited = [[False] * m for _ in range(n)]

for i in range(n):
    line = list(input())
    for j in range(m):
        graph[i][j] = int(line[j])

def bfs(x,y):
    queue = deque()
    queue.append((x,y))
    
    while queue:
        current = queue.popleft()
        
        for k in range(4):
            i = current[0] + dx[k]
            j = current[1] + dy[k]
            if i >= 0 and i < n and j >= 0 and j < m:
                if not visited[i][j] and graph[i][j] != 0:
                    graph[i][j] = graph[current[0]][current[1]] + 1
                    visited[i][j] = True
                    queue.append((i,j))
    
    
bfs(0,0)
print(graph[n-1][m-1])
    