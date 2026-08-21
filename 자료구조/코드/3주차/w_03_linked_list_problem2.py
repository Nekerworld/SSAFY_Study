# 2. 고장 난 객차 분리하기

# 현재 기차는 다음과 같이 연결되어 있다.
#
# 1호차 → 2호차 → 3호차 → 4호차
#
# 그런데 운행 도중 3호차에서 고장이 발생했다.
# 기차 전체를 다시 연결하지 않고,
# 3호차만 연결에서 제외해보자.

# [목표]
# 입력: 없음
# 출력: 1호차 → 2호차 → 4호차 → None

class TrainCar:
    def __init__(self, number):
        self.number = number
        self.next = None

# 객차 생성
car1 = TrainCar(1)
car2 = TrainCar(2)
car3 = TrainCar(3)
car4 = TrainCar(4)

# 1 → 2 → 3 → 4 연결
car1.next = car2
car2.next = car3
car3.next = car4

head = car1

# 3호차를 연결에서 제외하세요.
# 이 부분을 채우세요
None

# 현재 기차 출력
def print_train(head):
    current = head

    while current is not None:
        print(f"{current.number}호차", end=" → ")
        current = current.next

    print("None")

print_train(head)