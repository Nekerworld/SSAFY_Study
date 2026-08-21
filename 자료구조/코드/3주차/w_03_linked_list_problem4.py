# 4. 폭주 기관차

# 철도 시스템에 오류가 발생했다.
#
# 원래 기차는
#
# 1 → 2 → 3 → 4 → None
#
# 형태여야 한다.
#
# 그런데 4호차가 실수로 2호차를 다시 가리키게 되었다.
#
# 1 → 2 → 3 → 4
#     ↑         ↓
#     └─────────┘
#
# 이 상태에서는 next를 계속 따라가면
# 2 → 3 → 4 → 2 → 3 → 4...
# 무한 반복하게 된다.
#
# slow는 한 칸씩,
# fast는 두 칸씩 이동시켜
# 두 객차가 만나는지 확인해보자.

# [목표]
# 입력: 없음
# 출력: True

class TrainCar:
    def __init__(self, number):
        self.number = number
        self.next = None

# 객차 생성
car1 = TrainCar(1)
car2 = TrainCar(2)
car3 = TrainCar(3)
car4 = TrainCar(4)

# 객차 연결
car1.next = car2
car2.next = car3
car3.next = car4

# 오류 발생!
# 4호차가 다시 2호차를 가리킨다.
car4.next = car2

head = car1

def has_cycle(head):
    slow = head
    fast = head

    while fast is not None and fast.next is not None:

        # 이 부분을 채우세요.
        None

    return False

print(has_cycle(head))