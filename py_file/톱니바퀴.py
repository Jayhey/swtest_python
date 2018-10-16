from collections import deque

T = int(input())
tooth = [[0] for i in range(T)]
for i in range(T):
	tmp = str(input())
	tooth[i] = [int(s) for s in tmp]

t = int(input())
rotation = [[0] for _ in range(t)]
for i in range(t):
	a, b = list(map(int, input().split()))
	rotation[i] = [a - 1, b]


def rotate(wheel, direction):
	after = [0] * 8
	if direction == 1:  # 시계 방향
		for i in range(1, len(wheel)):
			after[i] = wheel[i - 1]
		after[0] = wheel[7]

	elif direction == -1:  # 반시계 방향
		for i in range(len(wheel) - 1):
			after[i] = wheel[i + 1]
		after[7] = wheel[0]
	else:  #
		after = wheel
	return after


def direction(tooth, rotation):
	d = [0] * len(tooth)
	r = rotation
	# 해당 톱니 기준 오른쪽 톱니
	d[r[0]] = r[1]
	for i in range(r[0], len(tooth) - 1):
		if tooth[i][2] != tooth[i + 1][6]:  # 극이 다를 경우
			d[i + 1] = -d[i]
		else:  # 극이 다를 경우
			d[i + 1] = 0
			break
	# 해당 톱니 기준 왼쪽 톱니
	for i in range(r[0], 0, -1):
		if tooth[i][6] != tooth[i - 1][2]:
			d[i - 1] = -d[i]
		else:
			d[i - 1] = 0
			break
	return d


for i in range(t):
	d = direction(tooth, rotation[i])
	for j in range(T):
		tooth[j] = rotate(tooth[j], d[j])

ans = 0
for i, wheel in enumerate(tooth):
	ans = ans + wheel[0]

print(ans)