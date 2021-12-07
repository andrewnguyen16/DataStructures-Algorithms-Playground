class Solution:
    def getDecimalValue(self, head) -> int:
        sum = head.val

        while head.next:
            second = head.next.val
            sum = (sum * 2) + second
            head = head.next

        return sum
