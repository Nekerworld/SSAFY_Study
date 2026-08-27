# 3. 프린터 작업 대기열

# 프린터에는 여러 문서가 순서대로 들어온다.
# 먼저 들어온 문서부터 하나씩 인쇄한다.
#
# PRINT 문서명 : 문서를 큐의 맨 뒤에 추가
# DONE         : 가장 오래 기다린 문서 1개를 인쇄하고 제거
#
# 모든 명령이 끝난 뒤
# 아직 인쇄되지 않은 문서들을 앞에서부터 출력하자.
#
# [명령]
# PRINT report
# PRINT photo
# DONE
# PRINT homework
# PRINT ticket
# DONE
#
# [출력]
# 남은 문서: homework ticket

from collections import deque

commands = [
    "PRINT report",
    "PRINT photo",
    "DONE",
    "PRINT homework",
    "PRINT ticket",
    "DONE",
]

printer_queue = deque()

for command in commands:
    parts = command.split()

    # PRINT라면 문서를 큐의 뒤에 넣고,
    # DONE이라면 큐의 앞 문서를 제거하세요.
    # 큐가 비어 있을 때 DONE이 들어오면 아무 작업도 하지 않습니다.
    None

print("남은 문서:", *printer_queue)
