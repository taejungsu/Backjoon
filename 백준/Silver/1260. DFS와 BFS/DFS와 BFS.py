def DFS(v):
    visited[v]=1
    dfs.append(v)
    for i in node[v]:
        if (visited[i]==0):
            DFS(i)

def BFS(v):
    visited[v]=1
    bfs.append(v)
    queue = [v]

    while(queue):
        for i in node[queue.pop(0)]:
            if(visited[i]==0):
                visited[i]=1
                bfs.append(i)
                queue.append(i)

N, M, V = map(int, input().split())

node =[[]for _ in range(N+1)]
visited = [0]*(N+1)
dfs = []
bfs = []

for i in range(M):
    a, b = map(int, input().split())
    node[a].append(b)
    node[b].append(a)

for j in range(N+1):
    node[j].sort()

DFS(V)
for j in range(N+1):
    visited[j]=0
BFS(V)

for m in dfs:
    print(m, end=' ')
print()
for n in bfs:
    print(n, end=' ')