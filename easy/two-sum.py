class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen_diffs = set()
        for i in range(len(nums)):
            if nums[i] in seen_diffs:
                return nums.index(target-nums[i]), i
            else:
                seen_diffs.add(target - nums[i])