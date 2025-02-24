def solution(A):
    A.sort()  # Sort the list first
    n = len(A)

    for i in range(n - 2):  # Loop to find triplets
        if (
            A[i] + A[i + 1] > A[i + 2]
        ):  # Check the triangle inequality for sorted triplet
            return 1
    return 0


print(solution([10, 2, 5, 1, 8, 20]))  # 1
print(solution([10, 50, 5, 1]))  # 0
print(solution([10, 50, 5, 1, 8, 20]))  # 1
print(solution([10, 50, 5, 1, 8, 20, 10]))  # 1
print(solution([10, 50, 5, 1, 8, 20, 10, 10]))  # 1
print(solution([10, 50, 5, 1, 8, 20, 10, 10, 10]))  # 1
