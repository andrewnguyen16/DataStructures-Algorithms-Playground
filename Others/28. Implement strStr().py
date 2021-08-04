class Solution:
    def strStr(self, haystack, needle):
        m = len(haystack)
        n = len(needle)
        if n == 0:
            return 0
        if m < n:
            return -1
        for i in range(m - n + 1):
            if haystack[i] != needle[0]:
                continue
            if haystack[i : i + len(needle)] == needle:
                return i
        return -1
