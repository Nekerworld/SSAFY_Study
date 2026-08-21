# 1. 스택 기본 연산 익히기

# 파이썬에서는 리스트를 스택처럼 사용할 수 있다.
# append() : 맨 위에 데이터 추가 -> push
# pop()    : 맨 위 데이터 제거 및 반환 -> pop
# stack[-1]: 맨 위 데이터 확인 -> peek/top

stack = []

# 접시를 10, 20, 30 순서로 쌓아보자.
stack.append(10)
stack.append(20)
stack.append(30)

print(stack)        # [10, 20, 30]
print(stack[-1])    # 30

removed = stack.pop()

print(removed)      # 30
print(stack)        # [10, 20]

# 가장 나중에 들어온 30이 가장 먼저 나왔다.
# 이것이 LIFO(Last In, First Out), 후입선출이다.
