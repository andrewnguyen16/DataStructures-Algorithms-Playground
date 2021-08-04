class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        f1 = head
        f2 = head
        while f2 and f2.next:
            f1 = f1.next
            f2 = f2.next.next
        return f1
