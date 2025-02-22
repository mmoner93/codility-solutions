def solution(A, K):
    if len(A) == 0:
        return A
    for i in range(K):
        first = A.pop()
        A = [first] + A
    return A
