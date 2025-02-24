def solution(A, B, K):
    if A % K == 0:
        return (B - A) // K + 1
    else:
        return (B - (A - A % K)) // K


print(solution(6, 11, 2))  # 3
print(solution(6, 11, 3))  # 2
