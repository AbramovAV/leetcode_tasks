class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if root:
            targetSum -= root.val
            if targetSum == 0 and root.left is root.right:
                return True
            return self.hasPathSum(root.left, targetSum) or self.hasPathSum(root.right, targetSum)
        return False