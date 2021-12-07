class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        hashmap = {}
        for num in nums:
            if num not in hashmap.keys():
                hashmap[num] = 1
            else:
                hashmap[num] = 0

        sum = 0
        for vv in hashmap.keys():
            if hashmap[vv] == 1:
                sum += vv

        return sum
