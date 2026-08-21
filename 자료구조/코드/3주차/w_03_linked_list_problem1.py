# 1. 기차 연결하기

# 기차의 객차들이 연결되어 있다.
# 각 객차는 다음 객차가 누구인지 알고 있다.
# 현재 기차는 1호차 → 2호차 → 4호차 순으로 연결되어 있다.
#
# 그런데 역에서 2호차와 4호차 사이에
# 3호차를 연결하라는 명령이 내려왔다.
# 연결 리스트를 사용하여 3호차를 추가해보자.

# [목표]
# 입력: 없음
# 출력: 1호차 → 2호차 → 3호차 → 4호차 → None

class TrainCar:
    def __init__(self, number):
        self.number = number
        self.next = None

# 객차 생성
car1 = TrainCar(1)
car2 = TrainCar(2)
car4 = TrainCar(4)

# 1 → 2 → 4 연결
car1.next = car2
car2.next = car4

head = car1

# 새로운 3호차 생성
car3 = TrainCar(3)

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