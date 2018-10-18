from copy import deepcopy

n = int(input())  # 지도 크기
k = int(input())  # 사과 갯수

apple = [[0] for _ in range(k)]
for i in range(k):
	a1, a2 = map(int, input().split())
	apple[i] = [a1-1, a2-1]

l = int(input())
move = []
for i in range(l):
	c, d = input().split()
	c = int(c)
	move.append([c,d])

tmp = deepcopy(move)
for i in range(1, len(move)):
	move[i][0] -= tmp[i-1][0]

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

d = 1
x, y = 0, 0

#apple_ = apple.copy()
apple = apple_.copy()
snake = [[x, y]]
sec = 0
cnt = 0
stop = False
for i in range(len(move)):
	time = move[i][0]
	for j in range(time):
		print("j :", j+1)
		if j == time - 1: # 마지막에 먼저 방향부터 정해주자
			print("방향 전환 중")
			if move[i][1] == 'D':
				d = (d + 1) % 4
			else:
				d = (d - 1) % 4
		print("방향 :", d)

		sec += 1
		nx = x + dx[d]  # 뱀 몸통 늘리기
		ny = y + dy[d]
		print("nx, ny : ",nx, ny)

		if 0 <= nx < n and 0 <= ny < n:
			x, y = nx, ny
			if [x, y] in snake[:-1]:
				stop = True
				print("몸통이랑 만남")
				break
			if [x, y] in apple:  # 사과가 있다면 사과가 없어지고 꼬리는 움직이지 않는다 (사과 제거)
				print('사과 있음')
				apple_idx = apple.index([x, y])
				apple.pop(apple_idx)
			elif [x, y] not in apple: # 사과 없으면 꼬리도 움직여
				print("사과 없음")
				snake.pop(0)
			elif [x, y] in snake[:-1]:  # 몸통 만나면 죽음
				stop = True
				print("몸통만남!")
				break
			snake.append([nx, ny])
			print(snake)
			print("-------")

		else:
			stop = True
			print("지도 밖임!")
			break

	if stop is True:
		print(sec)
		break


