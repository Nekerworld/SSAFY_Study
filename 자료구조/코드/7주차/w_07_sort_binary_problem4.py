# 4. 배송 번호를 병합 정렬로 정리하기

# 여러 배송 번호를 Merge Sort(병합 정렬)로 오름차순 정렬해보자.
#
# 병합 정렬의 흐름:
#
# 1. Divide  : 리스트를 절반으로 나눈다.
# 2. Conquer : 왼쪽과 오른쪽을 각각 재귀적으로 정렬한다.
# 3. Combine : 두 정렬된 리스트를 하나로 병합한다.
#
# 재귀적으로 나누는 부분은 미리 작성되어 있다.
# 이번 문제에서는 핵심인 "병합" 부분을 완성한다.
#
# [목표]
# 출력: [1, 2, 3, 4, 7, 8, 10, 12]


def merge(left, right):

    result = []

    i = 0
    j = 0

    while i < len(left) and j < len(right):

        # left[i]와 right[j]를 비교하여
        # 더 작은 값을 result에 추가하고
        # 해당 포인터를 한 칸 이동시키세요.
        None

    # 한쪽 리스트에 값이 남아 있다면
    # 남은 값들을 result 뒤에 이어 붙이세요.
    None

    return result


def merge_sort(data):

    if len(data) <= 1:
        return data

    mid = len(data) // 2

    # Divide + Conquer
    left = merge_sort(data[:mid])
    right = merge_sort(data[mid:])

    # Combine
    return merge(left, right)


delivery_numbers = [10, 3, 7, 1, 12, 2, 8, 4]

print(merge_sort(delivery_numbers))
