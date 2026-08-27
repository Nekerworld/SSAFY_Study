# 06. 해시 테이블 - Intro

# 이번 시간에는 Python의 dict와 set을 중심으로
# 해시 테이블을 간단하게 연습한다.
#
# Hash Table의 핵심 아이디어:
#
# Key를 이용해서 Value를 빠르게 저장하고 찾는다.
#
# 예)
# student = {
#     "민수": 90,
#     "지수": 85
# }
#
# "민수"가 Key
# 90이 Value


# =================================================================


# 1. Dictionary 기본 사용

scores = {}

# Key : Value 저장
scores["민수"] = 90
scores["지수"] = 85
scores["철수"] = 70

print(scores)

# Key를 이용해서 Value 조회
print(scores["민수"])   # 90
print(scores["지수"])   # 85


# =================================================================


# 2. 값 수정하기

# 이미 존재하는 Key에 새로운 값을 넣으면
# 기존 Value가 수정된다.

scores["민수"] = 100

print(scores["민수"])   # 100


# =================================================================


# 3. Key가 존재하는지 확인하기

menu = {
    "coffee": 3000,
    "tea": 2500,
    "juice": 4000
}

print("coffee" in menu)   # True
print("milk" in menu)     # False


# =================================================================


# 4. dict.get()

# 존재하지 않는 Key를 []로 바로 조회하면 오류가 발생할 수 있다.
#
# get()을 사용하면 Key가 없을 때
# 원하는 기본값을 반환할 수 있다.

print(menu.get("coffee"))          # 3000
print(menu.get("milk"))            # None
print(menu.get("milk", 0))         # 0


# =================================================================


# 5. Dictionary로 개수 세기

# 같은 데이터가 몇 번 등장했는지 셀 때
# Dictionary를 사용할 수 있다.

colors = ["red", "blue", "red", "green", "red", "blue"]

count = {}

for color in colors:

    if color in count:
        count[color] += 1
    else:
        count[color] = 1

print(count)
# {'red': 3, 'blue': 2, 'green': 1}


# get()을 이용하면 더 짧게 작성할 수도 있다.

count = {}

for color in colors:
    count[color] = count.get(color, 0) + 1

print(count)


# =================================================================


# 6. Dictionary 순회하기

prices = {
    "pen": 1000,
    "notebook": 2000,
    "eraser": 500
}

# Key 순회
for name in prices:
    print(name)

# Key와 Value를 함께 순회
for name, price in prices.items():
    print(name, price)


# =================================================================


# 7. Set 기본 사용

# Set은 중복된 값을 저장하지 않는다.

numbers = [1, 1, 2, 3, 3, 3, 4]

unique_numbers = set(numbers)

print(unique_numbers)
print(len(unique_numbers))   # 4


# =================================================================


# 8. Set에 데이터 추가하기

visited = set()

visited.add("A")
visited.add("B")
visited.add("A")

print(visited)

# A를 두 번 add해도
# Set에는 A가 하나만 존재한다.


# =================================================================


# 9. Set에서 존재 여부 확인하기

visited = {"A", "B", "C"}

print("A" in visited)   # True
print("D" in visited)   # False


# =================================================================


# 10. Hashable

# dict의 Key와 set의 원소는
# Hashable한 값이어야 한다.
#
# int, str 등은 사용할 수 있다.

example = {}

example[10] = "number"
example["apple"] = "string"

print(example)

# list는 값이 변경될 수 있는 Mutable 자료형이므로
# dict의 Key로 사용할 수 없다.
#
# 아래 코드는 실행하면 TypeError가 발생한다.
#
# example[[1, 2, 3]] = "list"


# =================================================================


# 핵심 정리
#
# dict
# Key : Value 형태로 데이터를 저장한다.
#
# data[key] = value
# data[key]
# key in data
# data.get(key, 기본값)
# data.items()
#
#
# set
# 중복을 허용하지 않는다.
#
# set(list)
# data.add(value)
# value in data
#
#
# 해시 테이블은 평균적으로
# 탐색 / 삽입 / 삭제를 빠르게 처리할 수 있다.
