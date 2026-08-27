# 7. 데크를 스택처럼, 큐처럼 사용하기

# 하나의 deque에 A, B, C를 순서대로 넣었다.
#
# 같은 deque라도
# 한쪽 끝만 사용하면 Stack처럼,
# 뒤에 넣고 앞에서 빼면 Queue처럼 사용할 수 있다.
#
# 아래 두 함수의 결과가 각각
# Stack 방식: C B A
# Queue 방식: A B C
# 가 되도록 완성해보자.

from collections import deque


def run_as_stack():
    dq = deque()

    dq.append("A")
    dq.append("B")
    dq.append("C")

    result = []

    while dq:
        # 가장 나중에 넣은 값부터 꺼내세요.
        None

    return result


def run_as_queue():
    dq = deque()

    dq.append("A")
    dq.append("B")
    dq.append("C")

    result = []

    while dq:
        # 가장 먼저 넣은 값부터 꺼내세요.
        None

    return result


print("Stack 방식:", *run_as_stack())   # C B A
print("Queue 방식:", *run_as_queue())   # A B C
