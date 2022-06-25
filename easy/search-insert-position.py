class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        left_ptr = 0
        right_ptr = len(nums)-1
        if target<=nums[0]: return 0
        elif target>nums[-1]: return len(nums)
        while right_ptr - left_ptr > 1:
            median = (left_ptr + right_ptr) // 2
            if nums[median] == target:
                return median
            elif nums[median] < target:
                left_ptr = median
            elif nums[median]>target:
                right_ptr = median
        return right_ptr