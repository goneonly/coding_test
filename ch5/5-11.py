# 5-11 4번 문제 - 미로 탈출

from collections import deque

n, m = map(int, input().split())

# 상 하 좌 우 정의
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

graph = []
for i in range(n):
    graph.append(list(map(int, input())))


def bfs(x, y):
    queue = deque()
    queue.append((x, y))   # 현 위치 push

    while queue:
        x, y = queue.popleft()   # 현 위치 pop

        # 1. 현 위치에서 네 방향 움직여보기
        for i in range(4):
            tempX = x + dx[i]
            tempY = y + dy[i]

            # 2-1. exception - out of boundary
            if (tempX < 0 or tempY < 0 or tempX >= n or tempY >= m):
                continue

            # 2-2. exception - 벽 (0) 무시
            if (graph[tempX][tempY] == 0):
                continue

            # 3. 해당 노드를 처음 방문시 기록 (push)
            if (graph[tempX][tempY] == 1):
                graph[tempX][tempY] = graph[x][y] + 1   # 현 위치 가중치 1 증가 (기록)
                queue.append((tempX, tempY))

    # 가장 오른쪽 아래 까지의 최단 거리 반환
    return graph[n-1][m-1]


print(bfs(0, 0))   # 위치는 0,0 으로 고정
