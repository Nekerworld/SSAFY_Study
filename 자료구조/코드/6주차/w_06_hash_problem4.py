# 4. 도서 대여 횟수 세기

# 도서관에서 하루 동안 대여된 책의 제목이 기록되어 있다.
#
# 각 책이 몇 번 대여되었는지 Dictionary에 저장하자.
#
# [기록]
# moon, star, moon, ocean, star, moon
#
# [목표]
# 출력:
# moon 3
# star 2
# ocean 1

records = ["moon", "star", "moon", "ocean", "star", "moon"]

count = {}

for title in records:

    # title이 처음 등장했다면 1,
    # 이미 count에 있다면 기존 값에 1을 더하세요.
    None

for title, number in count.items():
    print(title, number)
