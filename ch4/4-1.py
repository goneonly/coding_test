# 4-1 상하좌우

n = int(input())
x, y = 1, 1
plans = input().split()  # list

# L R U D 순으로 기준
move_types = ['L', 'R', 'U', 'D']
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

for plan in plans:
    for i in range(len(move_types)):
        if plan == move_types[i]:
            tempX = x + dx[i]
            tempY = y + dy[i]

    # 좌표 exception 체크
    if tempX < 1 or tempX < 1 or tempX > n or tempY > n:
        continue  # exception 이라 밑에 좌표를 옮기는 것을 확정짓는 코드를 스킵함
    x = tempX
    y = tempY

print(x, y)
