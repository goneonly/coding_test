# 6-12 4번 문제 - 두 배열의 원소 교체

n, k = map(int, input().split())  # 행렬 당 원소 개수 n, swap 연산 최대 횟수 k

A = list(map(int, input().split()))
B = list(map(int, input().split()))

A.sort()
B.sort(reverse=True)

for i in range(k):
    if (A[i] < B[i]):
        A[i], B[i] = B[i], A[i]  # swap
    else:
        break

print(sum(A))
