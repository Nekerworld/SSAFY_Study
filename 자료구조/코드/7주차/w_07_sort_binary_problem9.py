# 9. 창고 번호를 이분 탐색으로 찾기

# 창고 번호가 오름차순으로 정렬되어 있다.
# target 번호가 어느 인덱스에 있는지 Binary Search로 찾아보자.
#
# 반드시 left, right, mid를 직접 사용한다.
#
# [목표]
# target = 42
# 출력: 5

warehouse_numbers = [3, 8, 12, 19, 27, 42, 55, 68, 73]
target = 42

left = 0
right = len(warehouse_numbers) - 1
answer = -1

while left <= right:

    mid = (left + right) // 2

    if warehouse_numbers[mid] == target:
        answer = mid
        break

    elif warehouse_numbers[mid] < target:
        # target은 오른쪽에 있으므로
        # left를 이동시키세요.
        None

    else:
        # target은 왼쪽에 있으므로
        # right를 이동시키세요.
        None

print(answer)
