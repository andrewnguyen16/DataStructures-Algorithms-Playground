class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = [[]]
        temp = []
        for num in nums:
            length = len(res)
            for i in range(0, length):
                temp = [num] + res[i]
                res.append(temp)

        return res
