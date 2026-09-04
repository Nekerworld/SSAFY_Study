# 13. 순차 탐색과 이분 탐색의 비교 횟수 확인하기

# 같은 target을 두 가지 방법으로 찾아보자.
#
# Linear Search(순차 탐색)
# - 앞에서부터 하나씩 확인한다.
# - 정렬 여부와 상관없이 사용할 수 있다.
#
# Binary Search(이분 탐색)
# - 정렬된 데이터에서 탐색 범위를 절반씩 줄인다.
#
# 두 함수는 찾은 인덱스와 함께
# 몇 번 비교했는지도 반환한다.
#
# [목표]
# 두 방법 모두 target의 인덱스 15를 찾는다.
# 이분 탐색의 비교 횟수가 순차 탐색보다 적어야 한다.

numbers = [
    2, 5, 8, 12, 16, 23, 31, 38,
    45, 51, 57, 64, 70, 76, 83, 91
]

target = 91


def linear_search(arr, target):

    count = 0

    for i in range(len(arr)):

        count += 1

        # arr[i]가 target이면
        # (i, count)를 반환하세요.
        None

    return -1, count


def binary_search(arr, target):

    left = 0
    right = len(arr) - 1
    count = 0

    while left <= right:

        mid = (left + right) // 2
        count += 1

        # arr[mid]와 target을 비교해서
        # 찾았으면 (mid, count)를 반환하고,
        # 아니라면 left 또는 right를 이동시키세요.
        None

    return -1, count


linear_index, linear_count = linear_search(numbers, target)
binary_index, binary_count = binary_search(numbers, target)

print("순차 탐색:", linear_index, "비교", linear_count, "회")
print("이분 탐색:", binary_index, "비교", binary_count, "회")
