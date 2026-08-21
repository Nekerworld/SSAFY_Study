# 3. 올바른 괄호인지 검사하기

# '(' 와 ')' 로 이루어진 문자열이 주어진다.
# 괄호가 올바르게 짝지어져 있으면 True,
# 그렇지 않으면 False를 반환하자.
#
# 여는 괄호 '('를 만나면 스택에 넣고,
# 닫는 괄호 ')'를 만나면 가장 최근 '(' 하나를 꺼낸다.
#
# 주의할 점
# 1. 스택이 비어 있는데 ')'가 나오면 바로 False
# 2. 문자열을 모두 본 뒤 스택에 '('가 남아 있어도 False

# [예시]
# "(())()" -> True
# "(()"    -> False
# ")("     -> False


def is_valid_parentheses(text):
    stack = []

    for ch in text:

        # '(' 와 ')' 를 각각 어떻게 처리할지 작성하세요.
        None

    # 마지막에 스택이 비어 있어야 모든 괄호의 짝이 맞습니다.
    return None


print(is_valid_parentheses("(())()"))   # True
print(is_valid_parentheses("(()"))      # False
print(is_valid_parentheses(")("))       # False
