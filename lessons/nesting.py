def solution(S):
    opened = []
    for c in S:
        if c == "(":
            opened.append(c)
        elif c == ")" and opened and opened[-1] == "(":
            opened.pop()
        else:
            return 0
    return 1 if not opened else 0
