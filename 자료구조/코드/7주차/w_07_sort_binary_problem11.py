# 11. bisect로 검색 범위와 삽입 위치 처리하기

# 정렬된 도서 코드 목록이 있다.
#
# 이번 문제에서는 Python의 bisect 모듈을 사용한다.
#
# 1) code = 30이 몇 개 있는지 구한다.
#    bisect_left(), bisect_right() 사용
#
# 2) [20, 45] 범위에 속하는 코드의 개수를 구한다.
#
# 3) 새 코드 35를 정렬 상태를 유지하면서 삽입한다.
#    insort() 사용
#
# [목표]
# 30의 개수: 3
# 20~45 개수: 6
# 삽입 후: [10, 20, 30, 30, 30, 35, 40, 45, 50]

from bisect import bisect_left, bisect_right, insort

codes = [10, 20, 30, 30, 30, 40, 45, 50]

# 1. 값 30의 시작 위치와 끝 다음 위치를 구하세요.
left_index = None
right_index = None

print("30의 개수:", right_index - left_index)

# 2. [20, 45] 범위에 포함되는 원소 개수를 구하세요.
# 왼쪽 경계에는 bisect_left,
# 오른쪽 경계에는 bisect_right를 사용하세요.
range_count = None

print("20~45 개수:", range_count)

# 3. 새 코드 35를 정렬 상태를 유지하면서 삽입하세요.
None

print("삽입 후:", codes)
