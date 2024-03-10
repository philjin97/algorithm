import sys
sys.setrecursionlimit(10000)
input = sys.stdin.readline

from collections import deque
n, m, v = map(int, input().split())
graph = [[] for _ in range(n+1)]
visited_dfs = [False] * (n+1)
visited_bfs = [False] * (n+1)

for i in range(m):
    s, e = map(int, input().split())
    graph[s].append(e)
    graph[e].append(s)
 
for i in range(n+1):
    graph[i].sort()
    
def dfs(x):
    visited_dfs[x] = True
    print(x, end=' ')
    for i in graph[x]:
        if visited_dfs[i] == False:
            dfs(i)
    
def bfs(x):
    queue = deque()
    queue.append(x)
    visited_bfs[x] = True
    while queue:
        now = queue.popleft()
        print(now, end=' ')
        for i in graph[now]:
            if not visited_bfs[i]:
                visited_bfs[i] = True
                queue.append(i)
            
dfs(v)
print()
bfs(v)
    
