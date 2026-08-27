# 2. 큐 명령 처리하기

# 정수 큐 하나가 있다.
# 아래 명령들을 차례대로 처리해보자.
#
# push X : X를 큐의 맨 뒤에 넣는다.
# pop    : 큐의 맨 앞 값을 꺼내 출력한다. 비어 있으면 -1
# size   : 큐에 들어있는 값의 개수를 출력한다.
# empty  : 비어 있으면 1, 아니면 0을 출력한다.
# front  : 맨 앞 값을 출력한다. 비어 있으면 -1
# back   : 맨 뒤 값을 출력한다. 비어 있으면 -1
#
# [출력 예시]
# 10
# 20
# 2
# 20
# 30
# 0

from collections import deque

commands = [
    "push 10",
    "push 20",
    "front",
    "push 30",
    "pop",
    "size",
    "front",
    "back",
    "empty",
]

queue = deque()

for command in commands:
    parts = command.split()

    # 명령어 종류를 확인해서
    # append(), popleft(), len(), queue[0], queue[-1] 등을 사용해 처리하세요.
    # 비어 있는 큐에서 pop/front/back을 하려고 하면 -1을 출력해야 합니다.
    None
