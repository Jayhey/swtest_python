from collections import deque
from itertools import permutations, combinations

while True:
	w, h = map(int, input().split())

	if w == 0 and h == 0:
		break

	room = [[0] for _ in range(h)]
	for i in range(h):
		tmp = str(input())
		room[i] = [s for s in tmp]

	dx = [0, 0, -1, 1]
	dy = [-1, 1, 0, 0]

	dust = []
	visit = [[-1] * w for _ in range(h)]
	for i in range(h):
		for j in range(w):
			if room[i][j] == 'o':
				visit[i][j] = 0
				robot = [i, j]
			if room[i][j] == '*':
				dust.append([i, j])

	dust.insert(0, robot)

	if len(dust) == 1:  # 먼지가 없으면 0 출력
		print(0)
		continue



	def BFS(room, start, end):
		visit = [[-1] * w for _ in range(h)]
		visit[start[0]][start[1]] = 0
		que = deque([start])
		while que:
			pop = que.popleft()
			x, y = pop[0], pop[1]
			for k in range(4):
				nx = x + dx[k]
				ny = y + dy[k]
				if 0 <= nx < h and 0 <= ny < w:
					if room[nx][ny] == 'x':  # 벽이면 통과
						continue
					if [nx, ny] == end:
						visit[nx][ny] = visit[x][y] + 1
						return visit[nx][ny]
					if room[nx][ny] == "." and visit[nx][ny] == -1:  # 일반 바닥에 방문하지 않았다면?
						visit[nx][ny] = visit[x][y] + 1
						que.append([nx, ny])
		return 0

	comb = {}
	idx = list(combinations(range(len(dust)), 2))
	pair = list(map(list, combinations(dust, 2)))

	dist = {}
	for \
			i in range(len(pair)):
		dist[idx[i]] = BFS(room, pair[i][0], pair[i][1])
		dist[(idx[i][1], idx[i][0])] = dist[idx[i]]

	if 0 in dist.values():
		print(-1)
		continue

	route = list(map(list, permutations(range(1, len(dust)), 3)))
	for i in range(len(route)):
		route[i].insert(0, 0)

	ans = h * w
	for i in range(len(route)):
		tmp = 0
		stop = False
		for j in range(len(route[i])-1):
			tmp += dist[(route[i][j], route[i][j+1])]
			if tmp >= ans:
				stop = True
				continue
		if stop is True:
			continue
		ans = tmp

	if ans == h * w:
		print(-1)
	else:
		print(ans)