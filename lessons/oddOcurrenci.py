import time
from collections import Counter


def solution(A):
    count = Counter(A)
    for key, value in count.items():
        if value % 2 != 0:
            return key
    return None


# Test

start = time.time()
A = [999999999] * 100000000
A.append(1000000000)
print(solution(A))
print("Execution time: ", time.time() - start)

# Test A
start = time.time()
print(solution([9, 3, 9, 3, 9, 7, 9]))
print("Execution time: ", time.time() - start)

# Test B
start = time.time()
print(solution([1, 2, 3, 4, 5, 6, 7, 8, 19, 1, 2, 3, 4, 5, 6, 7, 8, 19, 19, 19, 19]))
print("Execution time: ", time.time() - start)

# Test C
start = time.time()
print(solution([1, 2, 3, 4, 5, 6, 7, 8, 20, 1, 2, 3, 4, 5, 6, 7, 8, 20, 20]))
print("Execution time: ", time.time() - start)
