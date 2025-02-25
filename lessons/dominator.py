from collections import Counter


def solution(A):
    if len(A) == 1:
        return 0
    elif len(A) < 3:
        return -1
    counter = Counter(A)
    dominator = max(counter, key=counter.get)
    if counter[dominator] > len(A) // 2:
        return A.index(dominator)
    return -1


print(solution([9, 3, 9, 3, 9, 7, 9, 9]))  # 7
print(solution([]))  # 0
print(solution([1]))  # 0
print(solution([1, 2]))  # 0
print(solution([1, 2, 3]))  # 0
print(solution([1, 2, 2]))  # 0
