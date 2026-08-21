# 1주차 자료구조 & 추상 자료형
# 리스트와 세트의 실행 시간 차이

import timeit

my_list = list(range(1_000_000))
my_set = set(range(1_000_000))
repeat_num = 100


list_time = timeit.timeit(
    "999999 in my_list",
    globals=globals(),
    number=repeat_num
)

set_time = timeit.timeit(
    "999999 in my_set",
    globals=globals(),
    number=repeat_num
)

list_elapsed_time = list_time / repeat_num * 1e6
set_elapsed_time = set_time / repeat_num * 1e6
print(f"평균 리스트 탐색 시간: {list_elapsed_time:.3f} μs/회")
print(f"평균 세트 탐색 시간 : {set_elapsed_time:.3f} μs/회")
print(f"리스트의 평균 탐색 시간은 세트의 {list_elapsed_time / set_elapsed_time:.2f}배 입니다.")
