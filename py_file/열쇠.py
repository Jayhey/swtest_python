from collections import deque

T = int(input())

for _ in range(T):
	h, w = map(int, input().split())

	room = [[0] for _ in range(h)]
	for i in range(h):
		tmp = "."+str(input())+"."
		room[i] = [s for s in tmp]

	room.insert(0, [s for s in "."*(w+2)])
	room.insert(len(room), [s for s in "."*(w+2)])

	upper = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R',
				'S','T','U','V','W','X','Y','Z']
	lower = [s.lower() for s in upper]
	door = {s:[] for s in upper}

	key = str(input())
	if key is '0':
		key = []
	else:
		key = [str(s).upper() for s in key]

	dx = [0,0,-1,1]
	dy = [-1,1,0,0]

	que = deque([[0,0]])
	room[0][0] = '1'

	cnt = 0
	while que:
		pop = que.pop()
		x, y = pop[0], pop[1]
		for k in range(4):
			nx = x + dx[k]
			ny = y + dy[k]
			if 0 <= nx < h+2 and 0 <= ny < w+2:
				if room[nx][ny] == '*': continue  # 벽이면 패스


				if 'A' <= room[nx][ny] <= 'Z':  # 문을 만났을 때
					if room[nx][ny] in key:  # 해당 문의 키를 가지고 있다면? 들어가자!
						room[nx][ny] = '1'
						que.append([nx,ny])
					else: # 키를 가지고 있지 않다면? door 딕셔너리에 추가해둠
						door[room[nx][ny]].append([nx, ny])
				if 'a' <= room[nx][ny] <= 'z': # 키를 만났다.
					key_wait = room[nx][ny].upper()
					key.append(key_wait)  # 소지하고 있는 키에 추가
					while door[key_wait]:  # 만약 door 대기열 있으면 없어질때까지
						wait = door[room[nx][ny].upper()].pop(0)
						room[wait[0]][wait[1]] = '1'
						que.append(wait)  # 큐 앞으로 넣자
					room[nx][ny] = '1'
					que.append([nx,ny])

				if room[nx][ny] == '$':
					room[nx][ny] = '1'
					cnt += 1
					que.append([nx, ny])
				if room[nx][ny] == '.':
					room[nx][ny] = '1'
					que.append([nx, ny])
	print(cnt)
