class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        self.travel = []

        def traveling(node):
            if node is None:
                return
            traveling(node.left)
            self.travel.append(node.val)
            traveling(node.right)

        traveling(root)
        return self.travel
