# Only Stack approach O(n)
def longestValidParentheses(s):
    l = len(s)
    stack = []
    for i in range(l):
        if stack and s[stack[-1]] == "(" and s[i] == ")":
            stack.pop()
        else:
            stack.append(i)

    if not stack:
        return l

    maxN = 0
    stack = [-1] + stack + [l]
    for i in range(len(stack) - 1):
        maxN = max(maxN, stack[i + 1] - stack[i] - 1)

    return maxN


print(longestValidParentheses("()(()))))"))
