# 5. 레이저로 쇠막대기 자르기

# '(' 는 쇠막대기의 시작 또는 레이저의 시작을 뜻하고,
# ')' 는 쇠막대기의 끝 또는 레이저의 끝을 뜻한다.
#
# "()" 처럼 바로 붙어 있는 괄호는 레이저다.
# 레이저가 나오면 현재 열려 있는 쇠막대기의 개수만큼 조각이 추가된다.
# 쇠막대기가 끝날 때는 마지막 조각 1개가 추가된다.
#
# 예시 문자열: "()((()))"
#
# 목표: 만들어지는 쇠막대기 조각의 총 개수를 계산하자.


def count_pieces(arrangement):
    stack = []
    pieces = 0

    for i in range(len(arrangement)):
        ch = arrangement[i]

        if ch == '(':
            stack.append(ch)

        else:
            # ')'를 만났으므로 '(' 하나를 제거합니다.
            # 바로 앞 문자가 '('였다면 레이저,
            # 바로 앞 문자가 ')'였다면 쇠막대기의 끝입니다.
            # 각각 pieces에 얼마를 더해야 할지 작성하세요.
            None

    return pieces


print(count_pieces("()((()))"))
