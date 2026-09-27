# 5-10 음료수 얼려 먹기
'''
0: 구멍이 뚫려있는 부분
1: 칸막이갖 존재하는 부분
목표: 그리드 내 0으로 연결된 부분의 개수를 카운트
'''

n, m = map(int, input().split())   # n * m 행렬 input

graph = []
for i in range(n):
    graph.append(list(map(int, input())))   # 2차원 배열 입력 받기


def dfs(x, y):
    # exception handling
    if (x <= -1 or x >= n or y <= -1 or y >= m):
        return False

    # main code
    if (graph[x][y] == 0):   # visited(0) 안되어있다면
        graph[x][y] = 1   # 우선 visited 마크
        # 순서대로 상 하 좌 우 재귀 호출
        dfs(x - 1, y)
        dfs(x + 1, y)
        dfs(x, y - 1)
        dfs(x, y + 1)
        return True

    return False   # otherwise


# main code
result = 0
for i in range(n):
    for j in range(m):
        if (dfs(i, j) == True):
            result += 1

print(result)
