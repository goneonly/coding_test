# 4. 1이 될 때까지

n, k = map(int, input().split())
result = 0

while n >= k:
    # n 이 k 로 나누어떨어지지 않는다면 빼기
    while n & k != 0:
        n -= 1
        result += 1
    # n 이 k 로 나누어지면 최대한 나누기
    n //= k
    result += 1

# 마무리로 1이 될때까지 빼기
while n > 1:
    n -= 1
    result += 1

print(result)
