class Solution:
    def removeDuplicates(self, lst: str) -> str:
        stack = []
        for c in lst:
            print(c)
            if stack != [] and stack[-1] == c:
                stack.pop()
            else:
                stack.append(c)
        return "".join(stack)
