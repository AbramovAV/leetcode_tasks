class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if root:
            values = []
            if root.left:
                values += self.inorderTraversal(root.left)
            values += [root.val]
            if root.right:
                values += self.inorderTraversal(root.right)
            return values
        return []