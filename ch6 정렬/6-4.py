# 6-4 퀵 정렬 O(n log n). 최악의 경우 O(N^2) when 이미 데이터가 정렬되어 있는 경우 가장 왼쪽 데이터를 pivot 으로 삼을 때

array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]   # 주어진 예제 배열


def quick_sort(array, start, end):
    if (start >= end):  # 원소가 1개인 경우 종료
        return
    pivot = start   # pivot 기준: 첫 번째 원소 (왼쪽)
    left = start + 1
    right = end
    while (left <= right):
        # pivot 보다 큰 데이터를 찾을 때까지 반복
        while (left <= end and array[left] <= array[pivot]):
            left += 1
        # pivot 보다 작은 데이터를 찾을 때까지 반복
        while (right > start and array[right] >= array[pivot]):
            right -= 1
        # 다 돌고 중앙에 두 데이터들만 남은 상황에서...
        if (left > right):  # 엇갈렸다면 작은 데이터와 pivot 을 교체
            array[right], array[pivot] = array[pivot], array[right]
        else:   # 엇갈리지 않았다면 작은 데이터와 큰 데이터를 교체
            array[left], array[right] = array[right], array[left]

    # 분할 이후 왼쪽 부분, 오른쪽 부분에서 각각 재귀적으로 정렬 수행
    quick_sort(array, 0, len(array) - 1)
    quick_sort(array, right + 1, end)


quick_sort(array, 0, len(array) - 1)
print(array)

'''
# 6-5 파이썬의 장점을 살린 퀵 정렬 소스코드

array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]   # 주어진 예제 배열

def quick_sort (array):
    # 리스트가 하나 이하의 원소만을 담고 있다면 종료
    if len(array) <= 1:
        return array
    
    pivot = array[0]
    tail = array[1:]

    left_side = [x for x in tail if x < pivot] # 분할된 왼쪽 부분
    right_side = [ x for x in tail if x > pivot] # 분할된 오른쪽 부분

    # 분할 이후 왼쪽 부분과 오른쪽 부분에서 각각 정렬을 수행하고, 전체 리스트를 반환
    return quick_sort (left_side) + [pivpt] + quick_sort(right_side)

print(quick_sort(array))
'''
