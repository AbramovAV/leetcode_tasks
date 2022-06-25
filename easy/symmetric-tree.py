class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        return root is None or self.compareNodes(root.left, root.right)
    
    def compareNodes(self, left: Optional[TreeNode], right: Optional[TreeNode]) -> bool:
        if left and right:
            if left.val == right.val:
                return self.compareNodes(left.left, right.right) and \
            self.compareNodes(left.right, right.left)
        
        return left is right