def solution(A):
    A = set(A)
    smallest_missing = 1
    while smallest_missing in A:
        smallest_missing += 1
    return smallest_missing


# print(solution([1, 3, 6, 4, 1, 2]))  # 5
print(solution([1, 2, 3]))  # 4
print(solution([-1, -3]))  # 1
print(solution([1]))  # 2
print(solution([2]))  # 1
print(solution([2, 1]))  # 3
print(solution([1, 2]))  # 3
print(solution([-1, 1]))  # 2
print(solution([-1, 2]))  # 2
