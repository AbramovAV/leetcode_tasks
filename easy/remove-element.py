class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        ptr_left = 0
        ptr_right = len(nums)
        while ptr_left < ptr_right:
            if nums[ptr_left] != val and nums[ptr_right-1] != val:
                ptr_left += 1
            elif nums[ptr_left] == val and nums[ptr_right-1] == val:
                ptr_right -= 1
            else:
                if nums[ptr_left] == val:
                    nums[ptr_left], nums[ptr_right-1] = nums[ptr_right-1], nums[ptr_left]
                ptr_left += 1
        return len(nums[:ptr_left])