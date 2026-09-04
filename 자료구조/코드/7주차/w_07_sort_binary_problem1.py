# 1. 점수표를 선택 정렬로 정리하기

# 체육대회 참가자들의 점수가 기록되어 있다.
# 점수를 오름차순으로 정렬하려고 한다.
#
# 이번 문제에서는 Python의 sort(), sorted()를 사용하지 않고
# Selection Sort(선택 정렬)를 직접 구현한다.
#
# 선택 정렬:
# 아직 정렬되지 않은 범위에서 가장 작은 값을 찾아
# 현재 위치와 교환한다.
#
# [입력 데이터]
# 73, 91, 68, 85, 77
#
# [목표]
# 출력: [68, 73, 77, 85, 91]

scores = [73, 91, 68, 85, 77]

for i in range(len(scores) - 1):

    min_index = i

    for j in range(i + 1, len(scores)):

        # scores[j]가 현재 최솟값보다 작다면
        # min_index를 j로 바꾸세요.
        None

    # i번째 값과 찾은 최솟값을 교환하세요.
    # Python의 a, b = b, a 방식을 사용하세요.
    None

print(scores)
