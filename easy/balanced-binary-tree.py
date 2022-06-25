class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if root:
            if abs(self.estimateDepth(root.left) - self.estimateDepth(root.right)) > 1:
                return False
            else:
                return self.isBalanced(root.left) and self.isBalanced(root.right)
        return True
    
    def estimateDepth(self, root:Optional[TreeNode]) -> int:
        depth = 0
        if root:
            depth = 1 + max(self.estimateDepth(root.left), self.estimateDepth(root.right))
        return depth