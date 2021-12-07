class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        div = floor(len(nums) / 2)
        dct = {}
        for num in nums:
            if num in dct:
                dct[num] += 1
            else:
                dct[num] = 1
            if dct[num] > div:
                return num
