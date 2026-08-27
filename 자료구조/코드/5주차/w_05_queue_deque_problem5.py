# 5. 원형 큐가 비었는지, 가득 찼는지 확인하기

# 원형 큐에서 한 칸을 항상 비워두는 방식을 사용한다.
#
# Empty 조건:
# front == rear
#
# Full 조건:
# (rear + 1) % capacity == front
#
# 아래 함수들을 완성해보자.

def is_empty(front, rear):
    # 큐가 비어 있으면 True, 아니면 False
    return None


def is_full(front, rear, capacity):
    # 큐가 가득 찼으면 True, 아니면 False
    return None


capacity = 5

print(is_empty(2, 2))             # True
print(is_empty(1, 3))             # False

print(is_full(0, 4, capacity))    # True
print(is_full(2, 0, capacity))    # False
