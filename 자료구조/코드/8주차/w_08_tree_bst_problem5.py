# 5. 도서 번호를 BST에서 빠르게 찾기

# 도서 번호가 BST에 저장되어 있다.
#
# target이 현재 노드보다 작으면 왼쪽,
# 크면 오른쪽으로 이동한다.
#
# 찾은 경우 해당 Node를 반환하고
# 없으면 None을 반환하도록 search()를 완성해보자.
#
# [목표]
# 60 -> 찾음
# 65 -> 없음


class BSTNode:

    def __init__(self, value):

        self.value = value
        self.left = None
        self.right = None


def insert(node, value):

    if node is None:
        return BSTNode(value)

    if value < node.value:
        node.left = insert(node.left, value)

    elif value > node.value:
        node.right = insert(node.right, value)

    return node


def search(node, target):

    # node가 None이면 탐색 실패
    # node.value == target이면 탐색 성공
    None

    # target이 현재 값보다 작으면 왼쪽,
    # 크면 오른쪽을 재귀적으로 탐색하세요.
    None


root = None

for value in [50, 30, 70, 20, 40, 60, 80]:
    root = insert(root, value)


for target in [60, 65]:

    result = search(root, target)

    if result is None:
        print(target, "-> 없음")

    else:
        print(target, "-> 찾음")
