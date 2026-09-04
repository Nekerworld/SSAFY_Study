# 10. 같은 점수가 시작하고 끝나는 위치 찾기

# 정렬된 시험 점수 목록에 같은 점수가 여러 번 등장한다.
#
# target 이상의 값이 처음 등장하는 위치 = Lower Bound
# target을 초과하는 값이 처음 등장하는 위치 = Upper Bound
#
# 두 함수를 직접 구현하고
# target이 몇 번 등장하는지도 계산해보자.
#
# [목표]
# lower: 2
# upper: 6
# count: 4

scores = [50, 60, 70, 70, 70, 70, 80, 90]
target = 70


def lower_bound(arr, target):

    left = 0
    right = len(arr)

    while left < right:

        mid = (left + right) // 2

        # arr[mid]가 target보다 작으면
        # lower bound는 오른쪽에 있다.
        # 그렇지 않으면 mid도 후보이므로 right를 mid로 옮긴다.
        None

    return left


def upper_bound(arr, target):

    left = 0
    right = len(arr)

    while left < right:

        mid = (left + right) // 2

        # arr[mid]가 target 이하이면
        # upper bound는 오른쪽에 있다.
        # 그렇지 않으면 mid도 후보이므로 right를 mid로 옮긴다.
        None

    return left


lower = lower_bound(scores, target)
upper = upper_bound(scores, target)

print("lower:", lower)
print("upper:", upper)
print("count:", upper - lower)
