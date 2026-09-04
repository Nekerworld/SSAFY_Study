# 08. 트리와 이진 탐색 트리(BST) - Intro

# 이번 시간에는
#
# 1. Tree 기본 구조와 용어
# 2. Binary Tree
# 3. Complete Binary Tree의 배열 표현
# 4. Tree Traversal
# 5. Binary Search Tree(BST)
# 6. BST Search / Insert / Delete
# 7. Balanced Tree와 Skewed Tree
#
# 를 간단한 코드와 함께 확인한다.


# =================================================================
# 1. Tree란?

# 트리는 계층적인 관계를 표현하는 비선형 자료구조이다.
#
# 예)
#
# 회사 조직도
# 폴더 구조
# 학교의 학과 구조
#
# 트리에서는 하나의 노드가
# 여러 개의 자식 노드를 가질 수 있다.
#
# 노드 수가 N개인 트리의 간선 수는 N - 1개이다.


# =================================================================
# 2. Tree 기본 용어

# Root
# - 트리의 가장 위에 있는 노드
#
# Parent
# - 어떤 노드의 바로 위 노드
#
# Child
# - 어떤 노드의 바로 아래 노드
#
# Leaf
# - 자식이 없는 노드
#
# Sibling
# - 같은 부모를 가진 노드
#
# Internal Node
# - 하나 이상의 자식을 가진 노드
#
# Subtree
# - 특정 노드를 새로운 Root로 생각했을 때 만들어지는 부분 트리


# =================================================================
# 3. TreeNode 만들기

class TreeNode:

    def __init__(self, value):

        self.value = value

        # 왼쪽 자식
        self.left = None

        # 오른쪽 자식
        self.right = None


# 간단한 이진 트리
#
#       A
#      / \
#     B   C
#    / \
#   D   E

root = TreeNode("A")

root.left = TreeNode("B")
root.right = TreeNode("C")

root.left.left = TreeNode("D")
root.left.right = TreeNode("E")

print("Root:", root.value)
print("A의 왼쪽 자식:", root.left.value)
print("A의 오른쪽 자식:", root.right.value)


# =================================================================
# 4. Depth와 Height

# 이번 강의에서는
#
# Root Depth = 0
# Leaf Height = 0
#
# 으로 사용한다.
#
# Depth
# - Root에서 특정 노드까지 내려갈 때 지나가는 간선 수
#
# Height
# - 특정 노드에서 가장 먼 Leaf까지 내려가는 간선 수
#
# 위 트리에서
#
# A의 Depth = 0
# B의 Depth = 1
# D의 Depth = 2
#
# D의 Height = 0
# B의 Height = 1
# A의 Height = 2


# =================================================================
# 5. Binary Tree

# Binary Tree(이진 트리)는
# 각 노드가 최대 2개의 자식을 가지는 트리이다.
#
# 왼쪽 자식과 오른쪽 자식은 서로 구분된다.
#
# 주의:
# Binary Tree라고 해서
# 값이 자동으로 정렬되어 있는 것은 아니다.


# =================================================================
# 6. Complete Binary Tree와 배열 인덱스

# Complete Binary Tree(완전 이진 트리)는
#
# 1. 마지막 Level을 제외한 모든 Level이 가득 차 있고
# 2. 마지막 Level은 왼쪽부터 차례대로 채워진 트리이다.
#
# 완전 이진 트리는 배열로 표현하기 좋다.
#
# 노드의 인덱스가 i일 때
#
# 왼쪽 자식 = 2 * i + 1
# 오른쪽 자식 = 2 * i + 2
# 부모       = (i - 1) // 2

tree_array = ["A", "B", "C", "D", "E", "F"]

i = 1

left_child_index = 2 * i + 1
right_child_index = 2 * i + 2
parent_index = (i - 1) // 2

print("현재 노드:", tree_array[i])
print("왼쪽 자식:", tree_array[left_child_index])
print("오른쪽 자식:", tree_array[right_child_index])
print("부모:", tree_array[parent_index])


# =================================================================
# 7. Tree는 재귀적인 구조

# 트리는 다음처럼 생각할 수 있다.
#
# Tree
# = Root
# + Left Subtree
# + Right Subtree
#
# 왼쪽 Subtree와 오른쪽 Subtree도
# 다시 하나의 Tree이기 때문에
# 재귀 함수와 매우 잘 어울린다.


# =================================================================
# 8. Preorder Traversal

# Preorder
#
# Root -> Left -> Right

def preorder(node):

    if node is None:
        return

    print(node.value, end=" ")

    preorder(node.left)
    preorder(node.right)


print("Preorder:", end=" ")
preorder(root)
print()


# =================================================================
# 9. Inorder Traversal

# Inorder
#
# Left -> Root -> Right

def inorder(node):

    if node is None:
        return

    inorder(node.left)

    print(node.value, end=" ")

    inorder(node.right)


print("Inorder:", end=" ")
inorder(root)
print()


# =================================================================
# 10. Postorder Traversal

# Postorder
#
# Left -> Right -> Root
#
# 자식 노드의 처리가 모두 끝난 뒤
# 부모를 처리해야 하는 작업에 잘 어울린다.

def postorder(node):

    if node is None:
        return

    postorder(node.left)
    postorder(node.right)

    print(node.value, end=" ")


print("Postorder:", end=" ")
postorder(root)
print()


# =================================================================
# 11. BST란?

# Binary Search Tree(BST)는
# Binary Tree에 "정렬 규칙"이 추가된 구조이다.
#
# 이번 강의에서는 중복 없는 Key를 기준으로 한다.
#
# Left Subtree의 모든 값
# <
# Current Node
# <
# Right Subtree의 모든 값
#
# 예)
#
#        50
#       /  \
#     30    70
#    / \    / \
#   20 40  60 80


# =================================================================
# 12. BST Node

class BSTNode:

    def __init__(self, value):

        self.value = value
        self.left = None
        self.right = None


# =================================================================
# 13. BST Insert

# 삽입할 값이 현재 노드보다 작으면 왼쪽,
# 크면 오른쪽으로 이동한다.

def insert(node, value):

    if node is None:
        return BSTNode(value)

    if value < node.value:
        node.left = insert(node.left, value)

    elif value > node.value:
        node.right = insert(node.right, value)

    return node


bst_root = None

for value in [50, 30, 70, 20, 40, 60, 80]:
    bst_root = insert(bst_root, value)


# =================================================================
# 14. BST Search

# 찾는 값이 현재 노드보다 작으면 왼쪽,
# 크면 오른쪽으로 이동한다.
#
# 트리 높이가 h라면
# 탐색 시간은 O(h)이다.
#
# 균형이 잘 잡혀 있다면
# 높이가 약 log N이므로 O(log N)에 가깝다.

def search(node, target):

    if node is None:
        return None

    if node.value == target:
        return node

    if target < node.value:
        return search(node.left, target)

    return search(node.right, target)


result = search(bst_root, 60)

if result is not None:
    print("BST Search 성공:", result.value)

else:
    print("BST Search 실패")


# =================================================================
# 15. BST의 Inorder Traversal

# BST를 Inorder로 순회하면
# 값이 오름차순으로 나온다.

print("BST Inorder:", end=" ")
inorder(bst_root)
print()


# =================================================================
# 16. BST Delete - 3가지 경우

# BST에서 노드를 삭제할 때는
# 자식 수에 따라 3가지 경우를 생각한다.
#
# 1. 자식이 0개
#    -> 그냥 제거
#
# 2. 자식이 1개
#    -> 자식 노드를 현재 위치로 올림
#
# 3. 자식이 2개
#    -> 오른쪽 Subtree의 최솟값
#       또는 왼쪽 Subtree의 최댓값으로 대체


def find_min(node):

    current = node

    while current.left is not None:
        current = current.left

    return current


def delete(node, value):

    if node is None:
        return None

    if value < node.value:
        node.left = delete(node.left, value)

    elif value > node.value:
        node.right = delete(node.right, value)

    else:

        # 자식이 0개 또는 오른쪽 자식만 있는 경우
        if node.left is None:
            return node.right

        # 왼쪽 자식만 있는 경우
        if node.right is None:
            return node.left

        # 자식이 2개인 경우
        successor = find_min(node.right)

        node.value = successor.value

        node.right = delete(node.right, successor.value)

    return node


bst_root = delete(bst_root, 20)
bst_root = delete(bst_root, 30)
bst_root = delete(bst_root, 50)

print("삭제 후 BST:", end=" ")
inorder(bst_root)
print()


# =================================================================
# 17. Skewed Tree

# BST라고 해서
# 탐색이 항상 O(log N)은 아니다.
#
# 정렬된 데이터를 그대로 삽입하면
# 한쪽으로 치우친 Skewed Tree가 만들어질 수 있다.
#
# 예)
#
# 10
#   \
#    20
#      \
#       30
#         \
#          40
#
# 이런 경우 높이가 N에 가까워지고
# 탐색도 최악의 경우 O(N)이 된다.

skewed_root = None

for value in [10, 20, 30, 40, 50]:
    skewed_root = insert(skewed_root, value)

print("편향 BST Inorder:", end=" ")
inorder(skewed_root)
print()


# =================================================================
# 18. Balanced Tree의 필요성

# BST의 성능은 트리의 높이에 크게 영향을 받는다.
#
# 균형이 잘 잡힌 트리
# -> 높이 약 O(log N)
#
# 한쪽으로 치우친 트리
# -> 높이 O(N)
#
# 그래서 AVL Tree, Red-Black Tree 같은
# Self-Balancing BST가 등장한다.


# =================================================================
# 19. 핵심 정리

# Tree
# - 계층형 비선형 자료구조
#
# Root / Parent / Child / Leaf
# Sibling / Internal Node / Subtree
#
# Depth
# - Root에서 내려간 간선 수
#
# Height
# - 가장 먼 Leaf까지의 간선 수
#
#
# Binary Tree
# - 자식 최대 2개
#
# Complete Binary Tree
# - 마지막 Level을 제외하고 가득 참
# - 마지막 Level은 왼쪽부터 채움
#
# 배열 인덱스
#
# left  = 2 * i + 1
# right = 2 * i + 2
# parent = (i - 1) // 2
#
#
# Traversal
#
# Preorder
# Root -> Left -> Right
#
# Inorder
# Left -> Root -> Right
#
# Postorder
# Left -> Right -> Root
#
#
# BST
#
# Left < Root < Right
#
# Search / Insert / Delete
#
# BST Inorder
# -> 오름차순 출력
#
# BST 탐색 시간
# -> O(h)
#
# 균형 트리
# -> O(log N)에 가까움
#
# 편향 트리
# -> 최악 O(N)
