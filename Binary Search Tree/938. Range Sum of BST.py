class Solution:
    def rangeSumBST(self, root: TreeNode, low: int, high: int) -> int:
        self.sum = 0

        def traveling(node):
            if node is None:
                return
            traveling(node.left)
            if low <= node.val <= high:
                self.sum += node.val
            traveling(node.right)

        traveling(root)
        return self.sum
