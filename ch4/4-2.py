# 4-2 시각
# 정수 n 이 입력되면 00시 00분 00초부터 N시 59분 59초까지의 모든 시각 중에서 3이 하나라도 포함되는 모든 경우의 수를 구해야함

n = int(input())
count = 0

# 3중 반복문
for h in range(n + 1):  # n 번 반복
    for m in range(60):
        for s in range(60):
            if '3' in (str(h) + str(m) + str(s)):  # hhmmss 에 '3' 이 있는가?
                count += 1


print(count)
