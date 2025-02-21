def solution(N):
    bin = []
    while N:
        bin.insert(0, N & 1)
        N = N >> 1
    max_gap = 0
    tmp_gap = 0
    for i in bin:
        if i == 0:
            tmp_gap += 1
        else:
            if tmp_gap > max_gap:
                max_gap = tmp_gap
            tmp_gap = 0
    return max_gap


print(solution(32))
print(solution(1041))
print(solution(9))
print(solution(529))
print(solution(20))
print(solution(15))
