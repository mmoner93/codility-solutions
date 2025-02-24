def solution(A):
    n = len(A)
    if n == 2:
        return 0

    min_avg_index = 0
    min_avg = (A[0] + A[1]) / 2

    for i in range(n - 2):
        avg_2 = (A[i] + A[i + 1]) / 2
        avg_3 = (A[i] + A[i + 1] + A[i + 2]) / 3

        if avg_2 < min_avg:
            min_avg = avg_2
            min_avg_index = i
        if avg_3 < min_avg:
            min_avg = avg_3
            min_avg_index = i

    # Check the last two elements
    avg_2 = (A[n - 2] + A[n - 1]) / 2
    if avg_2 < min_avg:
        min_avg = avg_2
        min_avg_index = n - 2

    return min_avg_index


print(solution([4, 2, 2]))  # 1
print(solution([4, 2, 2, 5, 1, 5, 8]))  # 1
print(solution([4, 2, 2, 5, 1, 5, 8, 1]))  # 1
print(solution([4, 2, 2, 5, 1, 5, 8, 1, 1, 1]))  # 1
