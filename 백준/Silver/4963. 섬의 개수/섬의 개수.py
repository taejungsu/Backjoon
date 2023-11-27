from collections import deque

dx = [-1,1,0,0,-1,+1,-1,+1]
dy = [0,0,-1,1,-1,-1,+1,+1]

def bfs(y,x):

    queue= deque()
    queue.append((y,x))
    while queue:
        y,x = queue.popleft()
        for i in range(8):
            nx = x+dx[i]
            ny = y+dy[i]

            if nx < 0 or nx >= w or ny < 0 or ny >= h:
                continue
            if graph[ny][nx]==0:
                continue

            if graph[ny][nx]==1:
                graph[ny][nx]=0
                queue.append((ny,nx))



while True:
    w,h = map(int,input().split())
    if w == 0 and h == 0 :
        break

    graph = []
    for _ in range(h):
        graph.append(list(map(int,input().split())))

    result = 0
    for i in range(h):
        for j in range(w):
            if graph[i][j] == 1:
                result += 1
                bfs(i,j)

    print(result)