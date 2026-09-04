# 07. 정렬과 이분 탐색 - Intro

# 이번 시간에는
#
# 1. 정렬(Sorting)
# 2. Python의 정렬 기능
# 3. 이분 탐색(Binary Search)
# 4. Lower Bound / Upper Bound
# 5. bisect 모듈
# 6. Parametric Search
#
# 를 간단한 코드로 확인한다.


# =================================================================
# 1. 왜 정렬이 필요한가?

# 정렬은 데이터를 일정한 기준에 따라 나열하는 것이다.
#
# 예)
# 오름차순 : 1, 2, 3, 4, 5
# 내림차순 : 5, 4, 3, 2, 1
#
# 데이터가 정렬되어 있으면
#
# - 최솟값 / 최댓값을 쉽게 확인할 수 있고
# - 같은 값끼리 모이므로 중복 확인이 쉬워지고
# - 이분 탐색을 사용할 수 있다.

numbers = [7, 2, 9, 1, 5]

print("원본:", numbers)
print("오름차순:", sorted(numbers))
print("내림차순:", sorted(numbers, reverse=True))


# =================================================================
# 2. Selection Sort - 가장 작은 값을 선택

# 선택 정렬은
# 아직 정렬되지 않은 범위에서 가장 작은 값을 찾고
# 현재 위치와 교환하는 방식이다.
#
# 시간 복잡도는 O(N^2)이다.

data = [64, 25, 12, 22, 11]

for i in range(len(data) - 1):

    min_index = i

    for j in range(i + 1, len(data)):
        if data[j] < data[min_index]:
            min_index = j

    data[i], data[min_index] = data[min_index], data[i]

print("선택 정렬:", data)


# =================================================================
# 3. Insertion Sort - 알맞은 위치에 삽입

# 삽입 정렬은
# 현재 값을 앞쪽의 정렬된 영역에
# 알맞은 위치로 삽입하는 방식이다.
#
# 큰 값들을 오른쪽으로 한 칸씩 밀고
# 빈 자리에 현재 값을 넣는다.
#
# 최악의 경우 O(N^2)이지만
# 이미 거의 정렬된 데이터에서는 매우 빠를 수 있다.

data = [12, 11, 13, 5, 6]

for i in range(1, len(data)):

    key = data[i]
    j = i - 1

    while j >= 0 and data[j] > key:
        data[j + 1] = data[j]
        j -= 1

    data[j + 1] = key

print("삽입 정렬:", data)


# =================================================================
# 4. Bubble Sort - 인접한 값 교환

# 버블 정렬은
# 서로 이웃한 두 값을 비교하고
# 순서가 잘못되어 있으면 교환한다.
#
# 한 번의 Pass가 끝날 때마다
# 가장 큰 값이 오른쪽 끝에 하나씩 확정된다.
#
# 교환이 한 번도 일어나지 않았다면
# 이미 정렬이 끝났으므로 조기 종료할 수 있다.

data = [5, 1, 4, 2, 8]

n = len(data)

for i in range(n - 1):

    swapped = False

    for j in range(0, n - 1 - i):

        if data[j] > data[j + 1]:
            data[j], data[j + 1] = data[j + 1], data[j]
            swapped = True

    if not swapped:
        break

print("버블 정렬:", data)


# =================================================================
# 5. Merge Sort - Divide & Conquer

# 병합 정렬은 분할 정복(Divide & Conquer)을 사용한다.
#
# Divide
# 리스트를 절반으로 나눈다.
#
# Conquer
# 나눈 두 부분을 각각 다시 정렬한다.
#
# Combine
# 두 정렬된 리스트를 하나로 합친다.
#
# 시간 복잡도는 O(N log N)이다.


def merge(left, right):

    result = []

    i = 0
    j = 0

    while i < len(left) and j < len(right):

        if left[i] <= right[j]:
            result.append(left[i])
            i += 1

        else:
            result.append(right[j])
            j += 1

    result.extend(left[i:])
    result.extend(right[j:])

    return result


def merge_sort(data):

    if len(data) <= 1:
        return data

    mid = len(data) // 2

    left = merge_sort(data[:mid])
    right = merge_sort(data[mid:])

    return merge(left, right)


data = [8, 3, 7, 4, 9, 2, 6, 5]

print("병합 정렬:", merge_sort(data))


# =================================================================
# 6. Quick Sort - Pivot을 기준으로 분할

# 퀵 정렬은 하나의 Pivot을 기준으로
#
# 작은 값
# 같은 값
# 큰 값
#
# 으로 나눈 뒤 각각 다시 정렬한다.
#
# 평균 시간 복잡도는 O(N log N)이다.
# 하지만 Pivot 선택이 좋지 않으면
# 최악의 경우 O(N^2)이 될 수 있다.


def quick_sort(data):

    if len(data) <= 1:
        return data

    pivot = data[len(data) // 2]

    left = [x for x in data if x < pivot]
    middle = [x for x in data if x == pivot]
    right = [x for x in data if x > pivot]

    return quick_sort(left) + middle + quick_sort(right)


data = [7, 3, 9, 2, 8, 5, 4]

print("퀵 정렬:", quick_sort(data))


# =================================================================
# 7. O(N^2) vs O(N log N)

# 선택 정렬, 삽입 정렬, 버블 정렬
# -> 대표적인 O(N^2) 정렬
#
# 병합 정렬, 퀵 정렬
# -> 대표적인 O(N log N) 정렬
#
# 데이터가 작을 때는 차이가 잘 느껴지지 않을 수 있지만
# 데이터가 커질수록 성능 차이가 매우 커진다.


# =================================================================
# 8. list.sort()와 sorted()

# list.sort()
# - 원본 리스트 자체를 정렬한다.
# - 반환값은 None이다.

numbers = [3, 1, 4, 2]

result = numbers.sort()

print("sort 후 원본:", numbers)
print("sort 반환값:", result)


# sorted()
# - 원본은 그대로 유지한다.
# - 정렬된 새로운 리스트를 반환한다.

numbers = [3, 1, 4, 2]

new_numbers = sorted(numbers)

print("sorted 후 원본:", numbers)
print("sorted 결과:", new_numbers)


# =================================================================
# 9. key와 lambda를 이용한 정렬

# key를 사용하면
# 어떤 값을 기준으로 정렬할지 직접 지정할 수 있다.

students = [
    ("Kim", 90, 80),
    ("Lee", 80, 100),
    ("Park", 90, 95),
]

# 국어 점수 오름차순
result = sorted(students, key=lambda x: x[1])

print("국어 오름차순:", result)


# 여러 조건도 튜플로 지정할 수 있다.
#
# 국어 점수 내림차순
# 동점이면 수학 점수 내림차순

result = sorted(students, key=lambda x: (-x[1], -x[2]))

print("국어/수학 내림차순:", result)


# =================================================================
# 10. Stable Sort - 같은 기준값의 순서 유지

# Stable Sort(안정 정렬)는
# 정렬 기준값이 같은 데이터들의
# 기존 상대적 순서를 유지하는 정렬이다.
#
# Python의 정렬은 Stable Sort이다.

reservations = [
    ("민수", "B"),
    ("유진", "A"),
    ("서준", "B"),
    ("하린", "A"),
]

# 구역만 기준으로 정렬한다.
# A끼리, B끼리는 기존 순서가 유지된다.

result = sorted(reservations, key=lambda x: x[1])

print("Stable Sort:", result)


# =================================================================
# 11. Linear Search와 Binary Search

# Linear Search(순차 탐색)
#
# 앞에서부터 하나씩 확인한다.
# 시간 복잡도는 O(N)이다.

numbers = [2, 5, 8, 12, 16, 23, 38, 56, 72, 91]
target = 23

found_index = -1

for i in range(len(numbers)):

    if numbers[i] == target:
        found_index = i
        break

print("순차 탐색:", found_index)


# Binary Search(이분 탐색)
#
# 반드시 데이터가 정렬되어 있어야 한다.
#
# left
# 현재 탐색 범위의 시작
#
# right
# 현재 탐색 범위의 끝
#
# mid
# 현재 탐색 범위의 중앙
#
# 한 번 비교할 때마다
# 탐색 범위를 절반으로 줄인다.
#
# 시간 복잡도는 O(log N)이다.

left = 0
right = len(numbers) - 1
answer = -1

while left <= right:

    mid = (left + right) // 2

    if numbers[mid] == target:
        answer = mid
        break

    elif numbers[mid] < target:
        left = mid + 1

    else:
        right = mid - 1

print("이분 탐색:", answer)


# =================================================================
# 12. Binary Search에서 중요한 점

# 1. 데이터가 반드시 정렬되어 있어야 한다.
#
# 2. 반복 조건은 보통
#    while left <= right
#
# 3. 오른쪽으로 이동할 때
#    left = mid + 1
#
# 4. 왼쪽으로 이동할 때
#    right = mid - 1
#
# +1, -1을 빼먹으면
# 같은 mid를 계속 확인하면서
# 무한 루프가 생길 수 있다.


# =================================================================
# 13. Lower Bound와 Upper Bound

# 중복된 값이 있는 정렬 배열에서는
# 단순히 "값이 존재하는가?"뿐 아니라
# 값이 시작하는 위치와 끝나는 위치가 필요할 수 있다.
#
# Lower Bound
# target 이상의 값이 처음 등장하는 위치
#
# Upper Bound
# target을 초과하는 값이 처음 등장하는 위치


def lower_bound(arr, target):

    left = 0
    right = len(arr)

    while left < right:

        mid = (left + right) // 2

        if arr[mid] < target:
            left = mid + 1

        else:
            right = mid

    return left


def upper_bound(arr, target):

    left = 0
    right = len(arr)

    while left < right:

        mid = (left + right) // 2

        if arr[mid] <= target:
            left = mid + 1

        else:
            right = mid

    return left


numbers = [1, 2, 4, 4, 4, 7, 9]

left_index = lower_bound(numbers, 4)
right_index = upper_bound(numbers, 4)

print("Lower Bound:", left_index)
print("Upper Bound:", right_index)
print("4의 개수:", right_index - left_index)


# =================================================================
# 14. Python bisect 모듈

# Python에서는 bisect 모듈을 사용하면
# Lower Bound와 Upper Bound를 쉽게 구할 수 있다.

from bisect import bisect_left, bisect_right, insort

numbers = [1, 2, 4, 4, 4, 7, 9]

left_index = bisect_left(numbers, 4)
right_index = bisect_right(numbers, 4)

print("bisect_left:", left_index)
print("bisect_right:", right_index)
print("4의 개수:", right_index - left_index)


# insort()
#
# 정렬된 상태를 유지하면서
# 새로운 값을 삽입한다.

insort(numbers, 5)

print("5 삽입 후:", numbers)


# =================================================================
# 15. bisect로 범위 안의 원소 개수 구하기

# [left_value, right_value] 범위에 포함되는
# 데이터의 개수를 구할 수 있다.
#
# 왼쪽 경계:
# bisect_left()
#
# 오른쪽 경계:
# bisect_right()

numbers = [1, 2, 3, 3, 3, 3, 4, 4, 8, 9]


def count_by_range(arr, left_value, right_value):

    left_index = bisect_left(arr, left_value)
    right_index = bisect_right(arr, right_value)

    return right_index - left_index


print("값이 3인 개수:", count_by_range(numbers, 3, 3))
print("2~7 사이 개수:", count_by_range(numbers, 2, 7))


# =================================================================
# 16. 정렬된 배열의 Trade-off

# 정렬된 배열은 이분 탐색을 사용하면
# 탐색을 O(log N)에 빠르게 처리할 수 있다.
#
# 하지만 중간에 새로운 값을 삽입하거나 삭제할 때는
# 뒤쪽 값들을 이동해야 할 수 있으므로
# 실제 삽입/삭제 비용은 O(N)이 될 수 있다.
#
# 즉,
#
# 탐색은 빠르지만
# 중간 삽입/삭제는 비용이 크다.


# =================================================================
# 17. Parametric Search

# Parametric Search는
# "최적값을 직접 찾는 문제"를
# "이 값이 가능한가?"라는 Yes / No 문제로 바꾸는 방법이다.
#
# 조건의 결과가
#
# True, True, True, False, False
#
# 처럼 한 방향으로 바뀌는 단조성이 있다면
# 이분 탐색으로 경계값을 찾을 수 있다.
#
# 예)
# 여러 케이블을 같은 길이로 잘라
# 최소 need개의 조각을 만들려고 한다.
#
# 질문을 다음처럼 바꾼다.
#
# "길이를 mid로 잘랐을 때
#  need개 이상 만들 수 있는가?"


cables = [120, 150, 90, 200]
need = 8

left = 1
right = max(cables)
answer = 0

while left <= right:

    mid = (left + right) // 2

    pieces = 0

    for cable in cables:
        pieces += cable // mid

    if pieces >= need:

        # 현재 길이로 충분한 개수를 만들 수 있다.
        # 더 긴 길이도 가능한지 확인한다.
        answer = mid
        left = mid + 1

    else:

        # 현재 길이가 너무 길다.
        # 더 짧은 길이를 확인한다.
        right = mid - 1

print("가능한 최대 케이블 길이:", answer)


# =================================================================
# 18. 핵심 정리

# 정렬
#
# Selection Sort
# - 최솟값을 선택해서 앞으로 보낸다.
#
# Insertion Sort
# - 정렬된 영역의 알맞은 위치에 값을 삽입한다.
#
# Bubble Sort
# - 인접한 두 값을 비교하고 교환한다.
#
# Merge Sort
# - Divide & Conquer
# - O(N log N)
#
# Quick Sort
# - Pivot을 기준으로 Partition
# - 평균 O(N log N)
#
#
# Python 정렬
#
# list.sort()
# - 원본 변경
#
# sorted()
# - 새로운 리스트 반환
#
# key=lambda
# - 원하는 정렬 기준 지정
#
# Python 정렬은 Stable Sort
#
#
# Binary Search
#
# 정렬된 데이터에서
# left, right, mid를 사용해
# 탐색 범위를 절반씩 줄인다.
#
# 시간 복잡도 O(log N)
#
#
# Lower Bound
# - target 이상의 값이 처음 등장하는 위치
#
# Upper Bound
# - target을 초과하는 값이 처음 등장하는 위치
#
#
# bisect_left()
# bisect_right()
# insort()
#
#
# Parametric Search
#
# 최적화 문제를 Yes / No 결정 문제로 바꾸고
# 단조성을 이용해서 경계값을 이분 탐색한다.
