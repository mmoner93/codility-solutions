def solution(A):
    n = len(A)
    if n == 0:
        return 0
    elif n == 1:
        if A[0] == 1:
            return 1
        else:
            return 0
    if set(A) == set(range(1, n + 1)):
        return 1
    else:
        return 0


print(solution([4, 1, 3, 2]))  # 1
print(solution([4, 1, 3]))  # 0

print(solution([1]))  # 1
print(solution([2]))  # 1
