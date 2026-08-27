# 6. 출입 기록 만들기

# 연구실 입구에서 출입한 사람의 이름을 기록한다.
#
# ENTER 이름 : 해당 사람이 연구실 안으로 들어온다.
# EXIT 이름  : 해당 사람이 연구실 밖으로 나간다.
#
# 현재 연구실 안에 있는 사람만 Set에 저장해보자.
#
# [명령]
# ENTER mina
# ENTER joon
# EXIT mina
# ENTER yuri
#
# [목표]
# 마지막에 joon과 yuri만 남아 있어야 한다.

commands = [
    "ENTER mina",
    "ENTER joon",
    "EXIT mina",
    "ENTER yuri"
]

inside = set()

for command in commands:
    action, name = command.split()

    # ENTER라면 add()를 사용해서 inside에 추가하세요.
    # EXIT라면 remove() 또는 discard()를 사용해서 제거하세요.
    None

print(inside)
