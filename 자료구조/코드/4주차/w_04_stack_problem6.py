# 6. 브라우저 뒤로 가기

# 브라우저에는 현재 페이지가 있고,
# VISIT 주소 명령을 받으면 새 페이지로 이동한다.
# BACK 명령을 받으면 바로 이전 페이지로 돌아간다.
#
# 뒤로 가기를 구현하기 위해
# 지금까지 방문한 페이지를 스택에 저장해보자.
#
# 규칙
# 1. VISIT 새주소: 현재 페이지를 스택에 넣고 새주소로 이동
# 2. BACK: 스택이 비어있지 않으면 가장 최근 페이지로 이동
# 3. BACK할 페이지가 없으면 현재 페이지 유지

# [명령]
# 시작 페이지: home
# VISIT news
# VISIT sports
# BACK
# VISIT weather
# BACK
# BACK

# [출력]
# 마지막 페이지는 home

commands = [
    "VISIT news",
    "VISIT sports",
    "BACK",
    "VISIT weather",
    "BACK",
    "BACK",
]

current = "home"
history = []

for command in commands:
    parts = command.split()

    # VISIT과 BACK을 구분해서
    # current와 history를 알맞게 변경하세요.
    None

print(f"마지막 페이지는 {current}")
