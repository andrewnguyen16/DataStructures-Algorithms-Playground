class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        hashTable = {}
        res = 0
        for i in nums:
            if i in hashTable:
                res += hashTable[i]
                hashTable[i] += 1
            else:
                hashTable[i] = 1
        return res
