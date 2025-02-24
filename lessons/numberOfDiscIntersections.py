def solution(A):
    result = 0
    N = len(A)
    if N < 2:
        return 0
    left = [0] * N
    right = [0] * N
    for i in range(N):
        left[i] = i - A[i]
        right[i] = i + A[i]
    left.sort()
    right.sort()
    j = 0
    for i in range(N):
        while j < N and right[i] >= left[j]:
            result += j
            result -= i
            j += 1
    if result > 10000000:
        return -1
    return result


print(solution([1, 5, 2, 1, 4, 0]))  # 11
print(solution([1, 1, 1]))  # 3
print(solution([1, 1, 1, 1]))  # 6
print(solution([1, 1, 1, 1, 1]))  # 10
print(solution([1, 1, 1, 1, 1, 1]))  # 15
