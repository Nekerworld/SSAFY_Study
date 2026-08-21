# 1. 노드 생성하기

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

node1 = Node(10)

print(node1.data)   # 10
print(node1.next)   # None

# 지금 이거 만든거임
# node1
# ┌──────────────┐
# │ data │ next  │
# │  10  │ None  │
# └──────────────┘



# =================================================================



# 2. 노드 여러 개 연결하기

node1 = Node(10)
node2 = Node(20)
node3 = Node(30)

node1.next = node2
node2.next = node3

head = node1

# 결과는 이러함
# head
#  ↓
# [10 | next] → [20 | next] → [30 | None]

# 여기서 node1.next = node2 이 코드는 
# "node1의 next가 node2를 참조한다" 라는 뜻임