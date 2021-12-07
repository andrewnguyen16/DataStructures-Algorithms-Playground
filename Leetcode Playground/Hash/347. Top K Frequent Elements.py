class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        res = []
        lst = sorted(Counter(nums).items(), key=lambda x: x[1], reverse=True)
        i = 0
        for key, value in lst:
            if i == k:
                break
            res.append(key)
            i += 1
        return res
