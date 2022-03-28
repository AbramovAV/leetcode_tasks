class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x<0:
            return False
        digits = []
        copy_x = x
        while copy_x > 0:
            digits.append(copy_x % 10)
            copy_x = copy_x // 10
        for digit in digits[::-1]:
            if digit != x%10:
                return False
            x = x // 10
        return True