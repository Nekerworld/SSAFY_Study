# 3. 폴더 구조를 세 가지 순서로 방문하기

# 폴더 구조가 다음 이진 트리처럼 저장되어 있다.
#
#        root
#       /    \
#    docs    src
#    /        / \
# notes    app  test
#
# Preorder  : Root -> Left -> Right
# Inorder   : Left -> Root -> Right
# Postorder : Left -> Right -> Root
#
# 세 순회 함수의 빈칸을 완성해보자.
#
# [목표]
#
# Preorder : root docs notes src app test
# Inorder  : notes docs root app src test
# Postorder: notes docs app test src root


class TreeNode:

    def __init__(self, value):

        self.value = value
        self.left = None
        self.right = None


root = TreeNode("root")

root.left = TreeNode("docs")
root.right = TreeNode("src")

root.left.left = TreeNode("notes")

root.right.left = TreeNode("app")
root.right.right = TreeNode("test")


def preorder(node):

    if node is None:
        return

    # Root -> Left -> Right
    None


def inorder(node):

    if node is None:
        return

    # Left -> Root -> Right
    None


def postorder(node):

    if node is None:
        return

    # Left -> Right -> Root
    None


print("Preorder:", end=" ")
preorder(root)
print()

print("Inorder:", end=" ")
inorder(root)
print()

print("Postorder:", end=" ")
postorder(root)
print()
