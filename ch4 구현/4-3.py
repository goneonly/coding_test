# 4-3 왕실의 나이트

'''
1. 수평으로 두 칸 이동한 뒤에 수직으로 한 칸 이동하기
2. 수직으로 두 칸 이동한 뒤에 수평으로 한 칸 이동하기
exception: 8x8 좌표 밖으로 나갈 수 없음

Q. 나이트의 위치가 주어졌을 때 나이트가 이동할 수 있는 경우의 수를 출력
'''

coordinate = input()
# a-h -> ord() 는 unicode 로 반환하는 메서드. 예를들어 b - a 는 98 - 97 = 1. 이때 index 시작 숫자는 1 이기에 여기에 1을 더해준다 = 2.
x = int(ord(coordinate[0])) - int(ord('a')) + 1  # row
y = int(coordinate[1])  # column, 1-8

# 나이트가 움직일 수 있는 8가지 방향
moves = [(2, 1), (-2, 1), (-2, -1), (2, -1),
         (1, 2), (-1, 2), (-1, -2), (1, -2)]

result = 0

for move in moves:
    next_row = x + move[0]
    next_column = y + move[1]

    # 좌표 확인
    if (next_row >= 1 and next_row <= 8 and next_column >= 1 and next_column <= 8):
        result += 1
print(result)
