# 6. 놀이공원 줄 앞뒤로 사람 넣기

# 어떤 놀이기구는 일반 손님은 줄의 뒤에 서고,
# 우선 탑승 손님은 줄의 앞에 설 수 있다.
#
# NORMAL 이름 : 줄의 뒤에 추가
# VIP 이름    : 줄의 앞에 추가
# ENTER        : 줄의 앞 사람을 입장시키고 출력
#
# Deque는 양쪽 끝에서 삽입과 삭제가 가능하다.
#
# [명령]
# NORMAL 민수
# NORMAL 지수
# VIP 소라
# ENTER
# NORMAL 준호
# ENTER
#
# [출력]
# 소라
# 민수

from collections import deque

commands = [
    "NORMAL 민수",
    "NORMAL 지수",
    "VIP 소라",
    "ENTER",
    "NORMAL 준호",
    "ENTER",
]

line = deque()

for command in commands:
    parts = command.split()

    # NORMAL은 append()
    # VIP는 appendleft()
    # ENTER는 popleft()
    # 를 사용해서 처리하세요.
    None
