# 7. 같은 BST인데 탐색 횟수가 다른 이유

# BST의 탐색 시간은 트리의 높이 h에 영향을 받는다.
#
# 균형이 잘 잡힌 BST
# -> 높이가 작아서 탐색이 빠르다.
#
# 한쪽으로 치우친 Skewed BST
# -> 높이가 커져서 최악 O(N)이 될 수 있다.
#
# 아래 두 BST에서 target = 70을 찾을 때
# 몇 개의 노드를 비교하는지 세어보자.
#
# [Balanced 삽입 순서]
# 40, 20, 60, 10, 30, 50, 70
#
# [Skewed 삽입 순서]
# 10, 20, 30, 40, 50, 60, 70
#
# [목표]
# Balanced 비교 횟수: 3
# Skewed 비교 횟수: 7


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


def search_count(node, target):

    count = 0

    current = node

    while current is not None:

        count += 1

        if current.value == target:
            return count

        # target과 current.value를 비교해서
        # current를 왼쪽 또는 오른쪽 자식으로 이동시키세요.
        None

    return count


balanced = None

for value in [40, 20, 60, 10, 30, 50, 70]:
    balanced = insert(balanced, value)


skewed = None

for value in [10, 20, 30, 40, 50, 60, 70]:
    skewed = insert(skewed, value)


print("Balanced 비교 횟수:", search_count(balanced, 70))
print("Skewed 비교 횟수:", search_count(skewed, 70))
