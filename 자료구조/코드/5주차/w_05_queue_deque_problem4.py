# 4. 원형 큐의 포인터 이동

# 크기가 5인 배열을 원형 큐처럼 사용하려고 한다.
# 마지막 인덱스 다음에는 다시 0번 인덱스로 돌아간다.
#
# 포인터를 한 칸 이동시키는 공식:
# (index + 1) % capacity
#
# 현재 rear가 3이다.
# Enqueue 연산이 4번 일어날 때마다
# rear의 위치를 출력해보자.
#
# [출력]
# 4
# 0
# 1
# 2

capacity = 5
rear = 3

for _ in range(4):

    # rear를 원형으로 한 칸 이동시키세요.
    None

    print(rear)
