class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []

        def create_permutations(path, arr):
            if not arr:
                res.append(path)
            for i in range(0, len(arr)):
                create_permutations(path + [arr[i]], arr[:i] + arr[i + 1 :])

        create_permutations([], nums)
        return res
