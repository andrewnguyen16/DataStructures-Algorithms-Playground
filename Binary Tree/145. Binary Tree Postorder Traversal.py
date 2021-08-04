class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        self.travel = []

        def helper(node):
            if not node:
                return
            helper(node.left)
            helper(node.right)
            self.travel.append(node.val)

        helper(root)
        return self.travel
