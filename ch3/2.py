# 2. 큰 수의 법칙
n, m, k = map(int, input().split())

# n 개의 자연수
data = list(map(int, input().split()))
data.sort()
first = data[n-1]
second = data[n-2]

result = 0

while True:
    for i in range(k):  # 가장 큰 수를 K번 더하기
        if m == 0:  # m 이 0 이라면 반복문 탈출
            break
        result += first
        m -= 1
    if m == 0:
        break
    result += second
    m -= 1

print(result)
