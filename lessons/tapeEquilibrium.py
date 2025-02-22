def solution(A):
    if len(A) == 1:
        return 0
    left_sum = A[0]
    right_sum = sum(A[1:])
    diff = abs(left_sum - right_sum)
    for i in range(1, len(A)):
        tmp_diff = abs(left_sum - right_sum)
        if diff == 0:
            return diff
        elif tmp_diff < diff:
            diff = tmp_diff
        left_sum += A[i]
        right_sum -= A[i]
    return diff


print(solution([3, 1, 2, 4, 3]))  # 1
print(solution([1, 2, 3, 4, 5]))  # 3
print(solution([1, 5]))  # 1
print(solution([1]))  # 1
print(solution([1, 2]))  # 1
print(solution([2, 1]))  # 1
print(solution([1, 2, 3]))  # 0
print(solution([3, 2, 1]))  # 0
