# 3. 사라진 객차를 찾아라

# 기차에는 수많은 객차가 연결되어 있다.
# 역무원은 특정 번호의 객차가
# 현재 기차에 연결되어 있는지 확인하려고 한다.
#
# 하지만 연결 리스트는 배열처럼
# 원하는 위치로 한 번에 이동할 수 없다.
#
# head부터 next를 하나씩 따라가면서
# 원하는 객차를 찾아보자.

# [목표]
# 입력: 없음
# 출력: 4호차를 찾았습니다!

class TrainCar:
    def __init__(self, number):
        self.number = number
        self.next = None


# 객차 생성
car1 = TrainCar(1)
car2 = TrainCar(2)
car3 = TrainCar(3)
car4 = TrainCar(4)
car5 = TrainCar(5)

# 객차 연결
car1.next = car2
car2.next = car3
car3.next = car4
car4.next = car5

head = car1

def find_car(head, target):
    current = head

    while current is not None:

        # 현재 객차가 찾는 객차인지 확인한 후 다음 객차로 이동
        None

    return None

result = find_car(head, 4)

if result is not None:
    print(f"{result.number}호차를 찾았습니다!")
else:
    print("해당 객차가 없습니다.")