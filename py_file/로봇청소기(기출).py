n, m = map(int, input().split())  # n : 세로, m : 가로

x, y, d = map(int, input().split())

room = [[None] * 50 for _ in range(50)]
for i in range(n):
	room[i] = list(map(int, input().split()))

dx = [-1, 0, 1, 0]  # 차례대로 북 서 남 동
dy = [0, 1, 0, -1]

while True:
	if room[x][y] == 0:
		room[x][y] = 2  # 1. 현재 위치 청소
	# 2-3, 2-4부터 체크하면 문제가 훨씬 편함. 사방이 청소 가능한지 확인
	if room[x + 1][y] != 0 and room[x - 1][y] != 0 and room[x][y - 1] != 0 and room[x][y + 1] != 0:
		if room[x - dx[d]][y - dy[d]] == 1:  # 뒤가 벽이면 멈춰
			break
		else:  # 뒤가 벽이 아니라면 후진
			x -= dx[d]
			y -= dy[d]
	# 2-1, 2-2 진행
	else:
		d = (d + 3) % 4
		if room[x + dx[d]][y + dy[d]] == 0:
			x += dx[d]
			y += dy[d]

ans = 0
for i in range(n):
	for j in range(m):
		if room[i][j] == 2:
			ans += 1
print(ans)