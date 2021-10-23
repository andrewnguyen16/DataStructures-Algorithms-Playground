class Solution:
    def balancedStringSplit(self, s: str) -> int:

        count = 0
        countBalanced = 0

        for i in range(0, len(s)):
            if s[i] == "R":
                count += 1
            if s[i] == "L":
                count -= 1
            if count == 0:
                countBalanced += 1

        return countBalanced
