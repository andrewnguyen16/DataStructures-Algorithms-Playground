class Solution:
    def sumRootToLeaf(self, root, val=0):
        if not root:
            return 0

        val = val * 2 + root.val

        if not root.left and not root.right:
            return val

        res = self.sumRootToLeaf(root.left, val) + self.sumRootToLeaf(root.right, val)

        return res
