class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        self.travel = []

        def helper(node):
            if not node:
                return
            self.travel.append(node.val)
            helper(node.left)
            helper(node.right)

        helper(root)
        return self.travel
