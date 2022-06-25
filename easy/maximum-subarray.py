class Solution:
    def maxSubArray(self, nums: List[int]) -> int: #Kadane's algo
        best_sum = float('-inf')
        current_sum = 0
        for num in nums:
            current_sum = max(num, current_sum + num)
            best_sum = max(current_sum, best_sum)
        return best_sum