# 1. 스택 명령 처리하기

# 정수 스택 하나가 있다.
# 아래 명령들을 차례대로 처리해보자.
#
# push X : X를 스택에 넣는다.
# pop    : 가장 위의 값을 꺼내 출력한다. 비어 있으면 -1
# size   : 스택에 들어있는 값의 개수를 출력한다.
# empty  : 비어 있으면 1, 아니면 0을 출력한다.
# top    : 가장 위의 값을 출력한다. 비어 있으면 -1

# [입력 예시]
# 7
# push 3
# push 5
# top
# size
# pop
# pop
# empty

# [출력 예시]
# 5
# 2
# 5
# 3
# 1

commands = [
    "push 3",
    "push 5",
    "top",
    "size",
    "pop",
    "pop",
    "empty",
]

stack = []

for command in commands:
    parts = command.split()

    # 명령어 종류를 확인해서
    # append(), pop(), len(), stack[-1] 등을 사용해 처리하세요.
    # 비어 있는 스택에서 pop/top을 하려고 하면 -1을 출력해야 합니다.
    None
