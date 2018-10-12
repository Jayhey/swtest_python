# 물이 차는 시간을 먼저 계산한 다음에 고슴도치 이동을 계산하면 된다!
# 이러면 동시 bfs 진행하는 경우보다 더 쉬움
from collections import deque

R, C = map(int, input().split())
forest = [0] * R
for i in range(R):
	tmp = str(input())
	forest[i] = [str(s) for s in tmp]

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

water = [[-1] * C for i in range(R)]  # 물 먼저 BFS 시작
visit = [[0] * C for i in range(R)]

arr = deque([])
arr_hog = deque([])
for i in range(R):
	for j in range(C):
		if forest[i][j] == '*':
			water[i][j] = 0
			arr.append([i, j])
		elif forest[i][j] == 'S':
			arr_hog.append([i, j])
		elif forest[i][j] == 'D':
			fx, fy = i, j

while arr:
	a, b = arr.popleft()
	for i in range(4):
		ax = a + dx[i]
		ay = b + dy[i]
		if ax >= 0 and ax < R and ay >= 0 and ay < C:
			if forest[ax][ay] == 'X': continue
			if forest[ax][ay] == 'D': continue
			if water[ax][ay] == -1:
				water[ax][ay] = water[a][b] + 1
				arr.append([ax, ay])

while arr_hog:
	a, b = arr_hog.popleft()
	for i in range(4):
		ax = a + dx[i]
		ay = b + dy[i]
		if ax >= 0 and ax < R and ay >= 0 and ay < C:
			if forest[ax][ay] == 'X': continue
			if visit[ax][ay] == 0 and visit[a][b] + 1 >= water[ax][ay]:
				visit[ax][ay] = visit[a][b] + 1
				arr_hog.append([ax, ay])


if visit[fx][fy] == 0:
	print("KAKTUS")
else:
	print(visit[fx][fy])
