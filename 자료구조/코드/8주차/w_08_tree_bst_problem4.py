# 4. 게임 랭킹 점수를 BST에 삽입하기

# 게임 랭킹 점수를 BST에 저장하려고 한다.
#
# BST 규칙:
#
# 왼쪽 Subtree의 값 < 현재 노드 < 오른쪽 Subtree의 값
#
# 중복 점수는 없다고 가정한다.
#
# [삽입 순서]
# 50, 30, 70, 20, 40, 60, 80
#
# 모든 값을 삽입한 뒤
# Inorder Traversal로 출력하면 오름차순이 되어야 한다.
#
# [목표]
# 출력: 20 30 40 50 60 70 80


class BSTNode:

    def __init__(self, value):

        self.value = value
        self.left = None
        self.right = None


def insert(node, value):

    # 비어 있는 위치를 만나면
    # 새로운 BSTNode를 만들어 반환하세요.
    None

    # value가 현재 노드보다 작으면 왼쪽,
    # 크면 오른쪽에 재귀적으로 삽입하세요.
    None

    return node


def inorder(node):

    if node is None:
        return

    inorder(node.left)

    print(node.value, end=" ")

    inorder(node.right)


root = None

scores = [50, 30, 70, 20, 40, 60, 80]

for score in scores:
    root = insert(root, score)

inorder(root)
