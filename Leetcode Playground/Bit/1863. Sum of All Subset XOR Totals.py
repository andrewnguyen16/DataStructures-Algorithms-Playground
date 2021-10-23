class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        result = 0
        for n in range(1 << len(nums)):
            term = 0
            for i in range(len(nums)):
                if n & 1:
                    term ^= nums[i]
                n >>= 1
            result += term
        return result
