def solution(A):
    if not A:
        return 1
    if len(A) == 1:
        if A[0] == 1:
            return 2
        else:
            return A[0] - 1
    A.sort()
    res = []
    for i in range(len(A) - 1):
        if A[i] + 1 != A[i + 1]:
            for i in range(A[i] + 1, A[i + 1]):
                res.append(i)
    if len(res) == 1:
        if A[0] == 1:
            return res[0]
        else:
            return A[0] - 1
    elif not res:
        if A[0] == 1:
            return A[-1] + 1
        else:
            return A[0] - 1
    else:
        return A[-1] + 1
    return res


print(solution([]))
print(solution([2]))
print(solution([1]))
print(solution([1, 2]))
print(solution([2, 3]))
print(solution([2, 3, 1, 5]))
print(solution([2, 3, 1, 5, 10]))
print(solution([21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 34]))
