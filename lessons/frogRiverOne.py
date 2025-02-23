def solution(X, A):
    leaves = set()
    for i in range(len(A)):
        leaves.add(A[i])
        if len(leaves) == X and X in leaves:
            return i
    return -1


print(solution(5, [1, 3, 1, 4, 2, 3, 5, 4]))  # 6
print(solution(4, [1, 3, 1, 4, 2, 3, 4]))  # -1
print(solution(1, [1]))  # 0
print(solution(1, [2]))  # -1
print(solution(1, [2, 1]))  # 1
print(solution(1, [1, 2]))  # 0
print(solution(1, [1, 1]))  # 0
print(solution(1, [1, 1, 1]))  # 0
print(solution(1, [1, 1, 2]))  # 0
print(solution(1, [1, 1, 1]))  # 0
