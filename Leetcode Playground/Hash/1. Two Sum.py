class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dct = dict()
        result = []
        for i in range(len(nums)):
            if target - nums[i] not in dct:
                dct[nums[i]] = i
            else:
                result.append(i)
                result.append(dct[target - nums[i]])
                return result
