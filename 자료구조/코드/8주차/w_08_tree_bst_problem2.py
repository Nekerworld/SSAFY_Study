# 2. 완전 이진 트리에서 가족 관계 찾기

# 완전 이진 트리를 배열로 표현하고 있다.
#
# 인덱스 공식:
#
# 왼쪽 자식 = 2 * i + 1
# 오른쪽 자식 = 2 * i + 2
# 부모       = (i - 1) // 2
#
# 아래 배열에서 index = 2인 노드의
# 부모, 왼쪽 자식, 오른쪽 자식을 출력해보자.
#
# [목표]
# 현재: C
# 부모: A
# 왼쪽 자식: F
# 오른쪽 자식: G

tree = ["A", "B", "C", "D", "E", "F", "G"]

i = 2

parent_index = None
left_index = None
right_index = None

print("현재:", tree[i])
print("부모:", tree[parent_index])
print("왼쪽 자식:", tree[left_index])
print("오른쪽 자식:", tree[right_index])
