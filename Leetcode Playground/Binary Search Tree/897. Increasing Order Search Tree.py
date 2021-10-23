class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:
        arr = []
        ans = curr = TreeNode()

        def helper(node):
            if not node:
                return
            helper(node.left)
            arr.append(node.val)
            helper(node.right)

        helper(root)

        for x in arr:
            curr.right = TreeNode(x)
            curr = curr.right

        return ans.right
