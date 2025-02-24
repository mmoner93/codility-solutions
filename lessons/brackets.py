def solution(S):
    opened = []
    for c in S:
        if c in ["(", "[", "{"]:
            opened.append(c)
        elif c == ")" and opened and opened[-1] == "(":
            opened.pop()
        elif c == "]" and opened and opened[-1] == "[":
            opened.pop()
        elif c == "}" and opened and opened[-1] == "{":
            opened.pop()
        else:
            return 0
    return 1 if not opened else 0


print(solution("{[()()]}"))  # 1
print(solution("([)()]"))  # 0
print(solution(")("))  # 0
print(solution("()"))  # 1
print(solution("()()"))  # 1
print(solution("()()()"))  # 1
print(solution("()()()("))  # 0
print(solution("()()()()"))  # 1
print(solution("()()()()("))  # 0
print(solution("()()()()()"))  # 1
