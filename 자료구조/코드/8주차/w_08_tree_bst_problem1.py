# 1. 회사 조직도의 Leaf 부서 찾기

# 회사 조직도가 이진 트리 형태로 저장되어 있다.
#
# 자식이 없는 노드를 Leaf Node라고 한다.
#
# 아래 트리에서 Leaf Node의 값을
# 왼쪽부터 출력해보자.
#
#        본사
#       /   \
#     개발   운영
#    /  \     \
#  웹   앱    인프라
#
# [목표]
# 출력: 웹 앱 인프라


class TreeNode:

    def __init__(self, value):

        self.value = value
        self.left = None
        self.right = None


root = TreeNode("본사")

root.left = TreeNode("개발")
root.right = TreeNode("운영")

root.left.left = TreeNode("웹")
root.left.right = TreeNode("앱")

root.right.right = TreeNode("인프라")


def print_leaves(node):

    if node is None:
        return

    # 왼쪽 자식과 오른쪽 자식이 모두 없다면
    # Leaf Node이므로 값을 출력하세요.
    None

    # 왼쪽과 오른쪽 Subtree도 재귀적으로 확인하세요.
    None


print_leaves(root)
