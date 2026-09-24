# 4-4 게임 개발

'''
첫째줄:
    n x m (세로 x 가로)
둘째줄:
    0: 북쪽
    1: 동쪽
    2: 남쪽
    3: 서쪽
셋째줄 (행렬):
    0: 육지
    1: 바다

Q.
1. 왼쪽으로 회전
2. 앞에 가본 길이 아니라면 움직임. 가본 길이라면 다시 1번으로
3. 만일 네 방향 모두 이미 가본 칸 / 바다 (1) 로 되어있는 칸은 바라보는 방향을 유지, 한 칸 뒤로 돌아감.
    - 만일 뒤로도 못 달아간다면 움직임을 멈춤. 끝
'''

# 첫째줄 (필드 크기 - 행렬)
n, m = map(int, input().split())

# 방문한 위치를 표기하기 위한 필드 초기화
d = [[0] * m for _ in range(n)]

# 둘째줄 (사용자 정보: 좌표, 방향)
x, y, direction = map(int, input().split())
d[x][y] = 1  # 현재 위치 방문 처리

# 셋째줄 (행렬 input)
array = []
for i in range(n):
    array.append(list(map(int, input().split())))


# 북 동 남 서 정의 (행렬 기준!!)
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]


def turn_left():
    # 왼쪽 회전
    global direction
    direction -= 1
    if direction == -1:
        direction = 3


# 시뮬레이션 시작
count = 1
turn_time = 0  # 3번 케이스를 위한 카운트

while (True):
    # 1. 왼쪽으로 회전
    turn_left()

    # 2. 앞에 가본 길이 아니라면 움직임. 가본 길이라면 다시 1번으로
    tempX = x + dx[direction]
    tempY = y + dy[direction]

    # 회전한 이후 정면에 가보지 않은 칸이 존재하는 경우 이동
    if (d[tempX][tempY] == 0) and (array[tempX][tempY] == 0):
        d[tempX][tempY] = 1  # 갔음을 체크
        x = tempX
        y = tempY
        count += 1
        turn_time = 0
        continue

    else:
        turn_time += 1  # 1번만 했으므로 카운트

    # 3. 만일 네 방향 모두 이미 가본 칸 / 바다 (1) 로 되어있는 칸은 바라보는 방향을 유지, 한 칸 뒤로 돌아감.
    if (turn_time == 4):
        tempX = x - dx[direction]
        tempY = y - dy[direction]

        # 뒤로 갈 수 있으면 돌아가기
        if array[tempX][tempY] == 0:
            x = tempX
            y = tempY
        else:
            # 종료; 못 움직임
            break
        turn_time = 0


print(count)
