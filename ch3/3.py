# 3. 숫자 카드 게임
# 각 행마다 가장 작은 수를 찾은 뒤에 그 수 중에서 가장 큰 수
n, m = int(input.split())  # 행, 열
result = 0

for i in range(n):
    data = list(map(int, input().split()))
    min_value = min(data)
    result = max(result, min_value)
print(result)
