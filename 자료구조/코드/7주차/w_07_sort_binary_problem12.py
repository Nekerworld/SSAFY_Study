# 12. 케이블을 같은 길이로 최대한 길게 자르기

# 길이가 서로 다른 케이블들이 있다.
# 모든 케이블을 같은 길이로 잘라서
# 최소 8개의 조각을 만들려고 한다.
#
# 가능한 조각 길이 중 가장 큰 값을 구하자.
#
# 이 문제는 Parametric Search(파라메트릭 서치) 문제이다.
#
# "길이를 X로 자르면 8개 이상 만들 수 있는가?"
#
# 라는 Yes/No 문제로 바꾼 뒤
# 가능한 길이의 최댓값을 이분 탐색으로 찾는다.
#
# [입력]
# cables = [120, 150, 90, 200]
# need = 8
#
# [목표]
# 출력: 60

cables = [120, 150, 90, 200]
need = 8

left = 1
right = max(cables)
answer = 0

while left <= right:

    mid = (left + right) // 2

    # 각 케이블을 길이 mid로 잘랐을 때
    # 만들 수 있는 총 조각 수를 계산하세요.
    pieces = None

    if pieces >= need:

        # mid 길이로 충분한 개수를 만들 수 있으므로
        # answer를 갱신하고 더 긴 길이를 시도하세요.
        None

    else:

        # 필요한 개수를 만들 수 없으므로
        # 더 짧은 길이를 시도하세요.
        None

print(answer)
