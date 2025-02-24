def solution(N, A):
    counter = [0] * N
    maximum = 0
    tmp_max = 0
    for inc in A:
        if inc == N + 1:
            maximum = tmp_max
        else:
            index = inc - 1
            if counter[index] < maximum:
                counter[index] = maximum
            counter[index] += 1
            tmp_max = max(tmp_max, counter[index])
    for i in range(N):
        if counter[i] < maximum:
            counter[i] = maximum
    return counter


print(solution(5, [3, 4, 4, 6, 1, 4, 4]))  # [3, 2, 2, 4, 2]
print(solution(1, [1]))  # [1]
print(solution(1, [2]))  # [0]
print(solution(1, [1, 1]))  # [2]
print(solution(1, [2, 2]))  # [0]
print(solution(1, [1, 2]))  # [1]
print(solution(1, [2, 1]))  # [1]
