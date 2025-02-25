def solution(A, B):
    if len(A) == 0:
        return 0
    elif len(A) == 1:
        return 1
    else:
        stack, alive_fishes = [], len(A)
        for fish in zip(A, B):
            if fish[1] == 1:
                stack.append(fish[0])
            else:
                while stack and stack[-1] < fish[0]:
                    stack.pop()
                    alive_fishes -= 1
                if stack:
                    alive_fishes -= 1
        return alive_fishes


print(solution([4, 3, 2, 1, 5], [0, 1, 0, 0, 0]))  # 2
print(solution([4, 3, 2, 1, 5], [0, 0, 0, 0, 0]))  # 5
print(solution([4, 3, 2, 1, 5], [1, 1, 1, 1, 1]))  # 5

# Test cases:
print(solution([4, 3, 2, 1, 5], [1, 0, 0, 0, 1]))  # 2
print(solution([6, 3, 2, 1, 5], [1, 0, 0, 0, 0]))  # 1
