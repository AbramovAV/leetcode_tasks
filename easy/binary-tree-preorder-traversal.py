class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        values = []
        if root:
            values = [root.val] + self.preorderTraversal(root.left) + \
            self.preorderTraversal(root.right)
        return values