# 1. 매표소 대기줄 처리하기

# 매표소 앞에 손님들이 줄을 서 있다.
# 먼저 줄을 선 손님이 먼저 표를 사는 FIFO 방식으로 처리한다.
#
# ARRIVE 이름 : 손님이 줄의 맨 뒤(Rear)에 선다.
# SERVE       : 줄의 맨 앞(Front) 손님을 처리하고 출력한다.
#               줄이 비어 있으면 "대기 손님 없음"을 출력한다.
#
# [명령]
# ARRIVE 민수
# ARRIVE 지수
# SERVE
# ARRIVE 철수
# SERVE
# SERVE
#
# [출력]
# 민수
# 지수
# 철수

from collections import deque

commands = [
    "ARRIVE 민수",
    "ARRIVE 지수",
    "SERVE",
    "ARRIVE 철수",
    "SERVE",
    "SERVE",
]

queue = deque()

for command in commands:
    parts = command.split()

    # ARRIVE라면 append()로 Rear에 추가하고,
    # SERVE라면 popleft()로 Front에서 제거하세요.
    # 비어 있는 큐에서 SERVE가 나오면 "대기 손님 없음"을 출력하세요.
    None
