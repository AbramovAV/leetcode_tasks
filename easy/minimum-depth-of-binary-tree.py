class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        depth = 0
        if root:
            if root.left is root.right:
                depth = 1
            elif root.left is None:
                depth = 1 + self.minDepth(root.right)
            elif root.right is None:
                depth = 1 + self.minDepth(root.left)
            else:
                depth = 1 + min(self.minDepth(root.left), self.minDepth(root.right))
        return depth