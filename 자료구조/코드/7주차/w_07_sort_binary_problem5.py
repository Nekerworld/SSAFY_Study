# 5. 퀵 정렬 방식으로 택배 무게 나누기

# 택배 상자 무게를 Quick Sort(퀵 정렬)의 방식으로 정렬해보자.
#
# 하나의 Pivot(피벗)을 정한 뒤
#
# pivot보다 작은 값  -> left
# pivot과 같은 값    -> middle
# pivot보다 큰 값    -> right
#
# 로 분할한 뒤 각각 다시 정렬한다.
#
# [목표]
# 출력: [2, 3, 4, 5, 7, 8, 9]

def quick_sort(data):

    if len(data) <= 1:
        return data

    pivot = data[len(data) // 2]

    # 아래 세 리스트를 완성하세요.
    left = None
    middle = None
    right = None

    # left와 right를 재귀적으로 quick_sort한 결과를
    # middle과 합쳐서 반환하세요.
    return None


weights = [7, 3, 9, 2, 8, 5, 4]

print(quick_sort(weights))
