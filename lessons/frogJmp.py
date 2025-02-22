def solution(X, Y, D):
    distance = Y - X
    min = distance // D
    if distance % D != 0:
        min += 1
    return min
