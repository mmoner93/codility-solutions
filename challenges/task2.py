# A word is diverse if it does not contain three equal consecutive letters (for
# example, "aaba" is diverse, but "aaab" is not).

# What is the alphabetically smallest diverse word that can be built using exactly
# A letters "a", B letters "b" and C letters "c"? A, B and C are chosen in such a way
# hat it is always possible to build such a word.

# Write a function:
# def solution(A, B, C)
# hat, given three integers A, B and C, returns the alphabetically smallest diverse
# word that can be built.

# Examples:
# 1. Given A = 3, B = 1 and C = 0, the function should return "aaba".
# 2. Given A = 1, B = 4 and C = 4, the function should return "abbcbcbcc".
# 3. Given A = 1, B = 3 and C = 0, the function should return "babb".
# Write an efficient algorithm for the following assumptions:


def solution(A, B, C):
    stack = ["", ""]
    counter = [A, B, C]
    s = []

    while sum(counter):
        for ind, letter in enumerate("abc"):
            if stack[0] == stack[1] and stack[0] == letter:
                continue
            if not counter[ind]:
                continue
            tmp_counter = list(counter)
            tmp_counter[ind] -= 1
            max_cnt = max(tmp_counter)
            sum_cnt_not_max = sum(tmp_counter) - max_cnt
            if max_cnt > sum_cnt_not_max * 2 + 2:
                continue
            stack[0] = stack[1]
            stack[1] = letter
            counter[ind] -= 1
            s.append(letter)
            break

    return "".join(s)


print(solution(3, 1, 0))  # aaba
print(solution(1, 4, 4))  # abbcbcbcc
print(solution(1, 3, 0))  # babb
