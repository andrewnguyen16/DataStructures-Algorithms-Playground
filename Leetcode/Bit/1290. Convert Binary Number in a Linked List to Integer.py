# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        sum = head.val

        while head.next:
            second = head.next.val
            sum = (sum * 2) + second
            head = head.next

        return sum
