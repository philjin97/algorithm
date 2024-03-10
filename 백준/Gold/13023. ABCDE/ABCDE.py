import sys
sys.setrecursionlimit(10000)
input = sys.stdin.readline 

arrive = False
n,m = map(int, input().split())
graph = [[] for _ in range(n+1)]
visited = [False] * (n+1)

#Save in graph 
for i in range(m):
    s,e = map(int, input().split())
    graph[s].append(e)
    graph[e].append(s)

#DFS
def dfs(x, cnt):
    global arrive
    if cnt == 5:
        arrive = True
        return
    #mark visited nodes, 재귀함수 
    visited[x] = True
    for i in graph[x]:
        if not visited[i]:
            dfs(i, cnt+1)
    visited[x] = False
    
#Start the DFS and Print
for i in range(1,n+1):
    dfs(i, 1)
    if arrive == True:
        break
if arrive == False:
    print(0)
else:
    print(1)