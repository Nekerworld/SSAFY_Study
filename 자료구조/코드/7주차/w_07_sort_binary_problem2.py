# 2. 거의 정렬된 출석 번호 정리하기

# 학생들의 출석 번호가 거의 정렬되어 있지만
# 일부 번호가 조금씩 어긋나 있다.
#
# 이런 데이터는 Insertion Sort(삽입 정렬)의 원리를
# 이해하기 좋은 예시이다.
#
# 두 번째 원소부터 하나씩 꺼내어
# 앞쪽의 정렬된 영역에서 알맞은 위치에 삽입한다.
#
# [입력 데이터]
# 1, 2, 5, 3, 4, 6
#
# [목표]
# 출력: [1, 2, 3, 4, 5, 6]

numbers = [1, 2, 5, 3, 4, 6]

for i in range(1, len(numbers)):

    key = numbers[i]
    j = i - 1

    # key보다 큰 값들을 오른쪽으로 한 칸씩 이동시키세요.
    while j >= 0 and numbers[j] > key:
        # numbers[j]를 numbers[j + 1]로 이동
        None

        # j를 한 칸 왼쪽으로 이동
        None

    # key를 알맞은 위치에 삽입하세요.
    None

print(numbers)
