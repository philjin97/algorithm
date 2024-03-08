import sys 
sys.setrecursionlimit(10000)

n, m = map(int, sys.stdin.readline().split())
visited = [False] * (n+1)
graph = [[] for _ in range(n+1)]

for _ in range(m):
    s, e = map(int, sys.stdin.readline().split())
    graph[s].append(e)
    graph[e].append(s)
   
def dfs(x):
    visited[x] = True
    for i in graph[x]:
        if visited[i] == False:
            dfs(i)
    
cnt = 0

for i in range(1, n+1):
    if visited[i] == False:
        cnt += 1
        dfs(i)
    
print(cnt)



