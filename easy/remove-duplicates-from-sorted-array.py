class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        ptr_unique = 0
        for ptr_dup in range(1,len(nums)):
            if nums[ptr_unique] != nums[ptr_dup]:
                ptr_unique += 1
                nums[ptr_unique] = nums[ptr_dup]
        return ptr_unique+1