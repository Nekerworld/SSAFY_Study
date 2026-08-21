# 4. 괄호 세 종류 검사하기

# 이번에는 (), [], {} 세 종류의 괄호가 섞여 있다.
# 모든 괄호의 종류와 순서가 정확히 맞으면 1,
# 하나라도 잘못되면 0을 반환하자.
#
# 예시
# "{[()]}"  -> 1
# "{[(])}"  -> 0
# "((()))"  -> 1
# "([)]"    -> 0


def check_brackets(text):
    stack = []

    # 닫는 괄호가 나왔을 때
    # 스택 맨 위에 어떤 여는 괄호가 있어야 하는지 표현한 딕셔너리
    pairs = {
        ')': '(',
        ']': '[',
        '}': '{'
    }

    for ch in text:

        # 여는 괄호라면 push
        # 닫는 괄호라면 stack의 top과 짝이 맞는지 확인 후 pop
        # 짝이 맞지 않으면 바로 0을 반환하세요.
        None

    # 모든 문자를 처리한 뒤 스택이 비어 있으면 1, 아니면 0
    return None


print(check_brackets("{[()]}"))   # 1
print(check_brackets("{[(])}"))   # 0
print(check_brackets("((()))"))   # 1
print(check_brackets("([)]"))     # 0
