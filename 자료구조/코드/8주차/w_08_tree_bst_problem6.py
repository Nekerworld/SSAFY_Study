# 6. BST에서 회원 번호 삭제하기

# BST에서 노드를 삭제할 때는
# 자식 수에 따라 3가지 경우가 있다.
#
# 1. 자식 0개
# 2. 자식 1개
# 3. 자식 2개
#
# 이번에는 자식이 2개인 노드를 삭제하는 경우까지 구현한다.
#
# 삭제 대상: 50
#
# 오른쪽 Subtree의 최솟값을 Successor로 사용한다.
#
# [목표]
# 삭제 전: 20 30 40 50 60 70 80
# 삭제 후: 20 30 40 60 70 80


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


def find_min(node):

    # 가장 왼쪽 노드까지 이동해서
    # 최솟값 Node를 반환하세요.
    None


def delete(node, value):

    if node is None:
        return None

    if value < node.value:
        node.left = delete(node.left, value)

    elif value > node.value:
        node.right = delete(node.right, value)

    else:

        # 왼쪽 자식이 없으면 오른쪽 자식을 반환
        # 오른쪽 자식이 없으면 왼쪽 자식을 반환
        None

        # 자식이 2개라면
        # 오른쪽 Subtree의 최솟값을 찾고
        # 현재 값을 그 값으로 바꾼 뒤
        # 오른쪽 Subtree에서 Successor를 삭제하세요.
        None

    return node


def inorder(node):

    if node is None:
        return

    inorder(node.left)

    print(node.value, end=" ")

    inorder(node.right)


root = None

for value in [50, 30, 70, 20, 40, 60, 80]:
    root = insert(root, value)

print("삭제 전:", end=" ")
inorder(root)
print()

root = delete(root, 50)

print("삭제 후:", end=" ")
inorder(root)
print()
