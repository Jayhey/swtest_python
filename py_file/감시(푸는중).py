n, m = map(int, input().split())

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]


a = [[0] for _ in range(n)]
for i in range(n):
	a[i] = list(map(int, input().split()))

wall = []
cctv = {i:[] for i in range(1,6)}

for i in range(n):
	for j in range(m):
		if a[i][j] == 6:
			wall.append([i,j])
		elif a[i][j] != 0:
			cctv[a[i][j]].append([i,j])

