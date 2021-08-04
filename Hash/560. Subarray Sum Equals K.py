class Solution:
    def subarraySum(self, arr, number):
        obj = {0: 1}
        count = 0
        sumx = 0
        for num in arr:
            sumx += num
            temp = sumx - number
            if temp in obj:
                count += obj[temp]
            if sumx in obj:
                obj[sumx] += 1
            else:
                obj[sumx] = 1
        return count
