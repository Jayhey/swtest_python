from collections import deque
from copy import deepcopy

h, w = map(int, input().split())

prison = [[0] for _ in range(h)]
for i in range(h):
    tmp = "."+str(input())+"."
    prison[i] = [s for s in tmp]

prison.insert(0, [s for s in "."*(w+2)])
prison.insert(len(prison), [s for s in "."*(w+2)])

prisoner = []
for i in range(h+1):
    for j in range(w+1):
        if prison[i][j] is "$": prisoner.append([i, j])
prisoner.append([0,0])

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

visit1 = [[-1 for _ in range(w+2)] for _ in range(h+2)]
visit2 = [[-1 for _ in range(w+2)] for _ in range(h+2)]
visit3 = [[-1 for _ in range(w+2)] for _ in range(h+2)]
def BFS(visit, prisoner):
    que = deque([prisoner])
    visit[prisoner[0]][prisoner[1]] = 0
    while que:
        arr = que.popleft()
        x, y = arr[0], arr[1]
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            if 0 <= nx < len(visit) and 0 <= ny < len(visit[0]):
                if visit[nx][ny] != -1: continue
                if prison[nx][ny] is '*': continue
                if prison[nx][ny] is '#':
                    visit[nx][ny] = visit[x][y] + 1
                    que.append([nx,ny])
                else:
                    visit[nx][ny] = visit[x][y]
                    que.appendleft([nx,ny])
    return visit

visit1 = BFS(visit1, prisoner[0])
visit2 = BFS(visit2, prisoner[1])
visit3 = BFS(visit3, prisoner[2])

ans = w * h
for i in range(h):
    for j in range(w):
        if prison[i][j] == '*': continue
        tmp = visit1[i][j] + visit2[i][j] + visit3[i][j]
        if prison[i][j] == '#': tmp -= 2
        if ans > tmp: ans = tmp

print(ans)