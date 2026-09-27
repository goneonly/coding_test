# 5-2 큐 예제

from collections import deque

queue = deque()

queue.append(1)  # 1 삽입
queue.append(2)  # 2 삽입
queue.append(3)  # 3 삽입
queue.popleft()  # (최상단) pop
print(queue)
queue.reverse()  # 역순으로 바꾸기
print(queue)
