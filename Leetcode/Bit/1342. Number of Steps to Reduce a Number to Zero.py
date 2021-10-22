class Solution:
    def numberOfSteps(self, num: int) -> int:
        if num == 0:
            return 0
        sum_ = 0

        while num != 0:
            if num & 1 == 0:
                sum_ += 1
            else:
                sum_ += 2
            num >>= 1

        return sum_ - 1
