class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        overflow = 1
        for i in range(len(digits)-1, -1, -1):
            overflow, digits[i] = (digits[i] + overflow) // 10, (digits[i] + overflow) % 10
        if overflow:
            digits = [overflow] + digits
        return digits