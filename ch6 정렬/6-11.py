# 6-11 3번 문제 - 성적이 낮은 순서로 학생 출력하기

n = int(input())

array = []


def get_value(data):
    return data[1]


for _ in range(n):
    input_data = input().split()
    # key - value 값으로 저장 - ( ) 써야함
    array.append((input_data[0], int(input_data[1])))

result = sorted(array, key=get_value)

for i in range(len(result)):
    print(result[i][0], end=' ')
