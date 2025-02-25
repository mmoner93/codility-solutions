def solution(H):
    stack, squares = [], 0
    for h in H:
        if not stack or h > stack[-1]:
            stack.append(h)
        elif h == stack[-1]:
            continue
        elif h < stack[-1]:
            while stack and h <= stack[-1]:
                if h != stack[-1]:
                    squares += 1
                stack.pop()
            stack.append(h)

    return squares + len(stack)


print(solution([8, 8, 5, 7, 9, 8, 7, 4, 8]))  # 7
print(solution([8, 8, 8, 8, 8, 8, 8, 8, 8]))  # 1
print(solution([8, 8, 8, 8, 8, 8, 8, 8, 7]))  # 2
print(solution([8, 8, 8, 8, 8, 8, 8, 7, 9]))  # 2
