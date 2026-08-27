# 1. Queue 기본 연산 익히기

# Queue(큐)는 먼저 들어온 데이터가 먼저 나오는 자료구조이다.
# FIFO (First In, First Out) = 선입선출
#
# enqueue : Queue의 Rear(뒤)에 데이터 추가
# dequeue : Queue의 Front(앞)에서 데이터 제거
#
# Python에서는 collections.deque를 사용하면
# Queue의 enqueue, dequeue를 효율적으로 구현할 수 있다.

from collections import deque

queue = deque()

# A, B, C 순서로 Queue에 넣기
queue.append("A")
queue.append("B")
queue.append("C")

print(queue)       # deque(['A', 'B', 'C'])
print(queue[0])    # A : Front
print(queue[-1])   # C : Rear

removed = queue.popleft()

print(removed)     # A
print(queue)       # deque(['B', 'C'])

# 가장 먼저 들어온 A가 가장 먼저 나왔다.
# 이것이 FIFO(First In, First Out), 선입선출이다.


# =================================================================


# 2. Enqueue & Dequeue 확인하기

queue = deque([10, 20, 30])

# 현재 상태
# Front                 Rear
#   ↓                     ↓
# [10] ← [20] ← [30]

# Enqueue
# 데이터는 Rear(뒤)에 추가된다.
queue.append(40)

print(queue)       # deque([10, 20, 30, 40])

# Dequeue
# 데이터는 Front(앞)에서 제거된다.
item = queue.popleft()

print(item)        # 10
print(queue)       # deque([20, 30, 40])


# =================================================================


# 3. Queue와 Stack의 차이

# 같은 A, B, C를 넣어도
# 꺼내는 위치에 따라 결과가 달라진다.

stack = deque()
queue = deque()

for data in ["A", "B", "C"]:
    stack.append(data)
    queue.append(data)

# Stack
# 한쪽 끝에서 넣고 한쪽 끝에서 꺼낸다.
# LIFO : C → B → A

print("Stack:", end=" ")

while stack:
    print(stack.pop(), end=" ")

print()


# Queue
# 뒤에서 넣고 앞에서 꺼낸다.
# FIFO : A → B → C

print("Queue:", end=" ")

while queue:
    print(queue.popleft(), end=" ")

print()


# =================================================================


# 4. Circular Queue의 포인터 이동

# 고정 크기 배열을 Queue로 사용할 때
# Rear가 배열의 마지막에 도착했다고 해서
# 앞쪽의 빈 공간을 버릴 필요는 없다.
#
# 배열의 마지막 다음을 다시 0번 인덱스로 연결하면 된다.
# 이 구조를 Circular Queue(원형 큐)라고 한다.
#
# 포인터 이동 공식
# (index + 1) % capacity

capacity = 5
rear = 3

print("현재 rear:", rear)     # 3

rear = (rear + 1) % capacity
print("이동 후:", rear)       # 4

rear = (rear + 1) % capacity
print("한 번 더 이동:", rear) # 0

# (4 + 1) % 5 = 0
# 마지막 인덱스 다음에는 다시 처음으로 돌아간다.


# =================================================================


# 5. Circular Queue의 Empty / Full

# 한 칸을 항상 비워두는 방식의 원형 큐에서는
#
# Empty
# front == rear
#
# Full
# (rear + 1) % capacity == front

capacity = 5

front = 2
rear = 2

print(front == rear)                       # True : Empty


front = 0
rear = 4

print((rear + 1) % capacity == front)      # True : Full

# capacity가 5여도
# Empty와 Full을 구분하기 위해 한 칸을 비워두므로
# 실제로 저장할 수 있는 데이터는 최대 4개이다.


# =================================================================


# 6. Deque 기본 연산 익히기

# Deque(Double-Ended Queue)는
# Front와 Rear 양쪽에서
# 데이터 삽입과 삭제가 모두 가능한 자료구조이다.

dq = deque(["A", "B", "C"])

print(dq)              # deque(['A', 'B', 'C'])

# Rear(오른쪽)에 추가
dq.append("D")

print(dq)              # deque(['A', 'B', 'C', 'D'])

# Front(왼쪽)에 추가
dq.appendleft("Z")

print(dq)              # deque(['Z', 'A', 'B', 'C', 'D'])

# Rear에서 제거
right_item = dq.pop()

print(right_item)      # D
print(dq)              # deque(['Z', 'A', 'B', 'C'])

# Front에서 제거
left_item = dq.popleft()

print(left_item)       # Z
print(dq)              # deque(['A', 'B', 'C'])


# =================================================================


# 7. deque의 핵심 연산 정리

#                  Front                  Rear
#                    ↓                      ↓
#                [ A ][ B ][ C ]
#
# append(x)      : Rear에 x 추가
# appendleft(x)  : Front에 x 추가
# pop()          : Rear 데이터 제거 및 반환
# popleft()      : Front 데이터 제거 및 반환
#
# collections.deque는
# 양쪽 끝의 추가/삭제 연산을 O(1)에 처리할 수 있다.
#
# Queue로 사용할 때는 보통
#
# enqueue -> append()
# dequeue -> popleft()
#
# 형태로 사용한다.
