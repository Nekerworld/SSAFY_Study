# 3. 온도 기록을 버블 정렬로 정리하기

# 실험실에서 측정한 온도 기록을 오름차순으로 정렬하려고 한다.
#
# Bubble Sort(버블 정렬)는
# 서로 인접한 두 값을 비교하여 순서가 잘못되어 있으면 교환한다.
#
# 한 번의 Pass가 끝날 때마다
# 가장 큰 값 하나가 오른쪽 끝에 확정된다.
#
# 이미 정렬이 끝났다면 더 이상 반복하지 않도록
# swapped 변수를 이용한 조기 종료도 구현해보자.
#
# [목표]
# 출력: [18, 19, 20, 21, 22]

temperatures = [22, 19, 21, 18, 20]

n = len(temperatures)

for i in range(n - 1):

    swapped = False

    for j in range(0, n - 1 - i):

        # 왼쪽 값이 오른쪽 값보다 크다면 두 값을 교환하고
        # swapped를 True로 바꾸세요.
        None

    # 이번 Pass에서 한 번도 교환하지 않았다면
    # 이미 정렬된 상태이므로 반복을 종료하세요.
    None

print(temperatures)
