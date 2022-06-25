class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        depth = 0
        if root:
            depth = 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))
        return depth