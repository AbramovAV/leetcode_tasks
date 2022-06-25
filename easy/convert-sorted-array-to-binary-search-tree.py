class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        middle = (0 + len(nums)-1) // 2
        node = TreeNode(val = nums[middle])
        if middle:
            node.left = self.sortedArrayToBST(nums[:middle])
        if len(nums)-1 > middle:
            node.right = self.sortedArrayToBST(nums[middle+1:])
        return node