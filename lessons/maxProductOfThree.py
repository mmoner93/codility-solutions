def solution(A):
    A.sort()
    n = len(A)
    return max(
        A[0] * A[1] * A[n - 1], A[n - 1] * A[n - 2] * A[n - 3], A[0] * A[1] * A[2]
    )


print(solution([-3, 1, 2, -2, 5, 6]))  # 60
print(solution([-5, 5, -5, 4]))  # 125
print(solution([-5, -5, -5, -5]))  # -125
print(solution([0, 0, 0, 0]))  # 0
print(solution([0, 0, 0, 1]))  # 0
print(solution([0, 0, 1, 1]))  # 0
print(solution([0, 1, 1, 1]))  # 1
print(solution([1, 1, 1, 1]))  # 1
print(solution([1, 1, 1, 2]))  # 2
print(solution([1, 1, 2, 2]))  # 4
