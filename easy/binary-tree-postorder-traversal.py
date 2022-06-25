class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        values = []
        if root:
            values += self.postorderTraversal(root.left) + self.postorderTraversal(root.right) + [root.val]
        return values