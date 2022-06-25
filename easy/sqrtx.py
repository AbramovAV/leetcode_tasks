class Solution:
    def mySqrt(self, x: int) -> int:
        left_ptr = 0
        right_ptr = x // 2
        while right_ptr>=left_ptr:
            median = (right_ptr + left_ptr) // 2
            if median ** 2 <= x and (median+1) ** 2 > x:
                return median
            if median ** 2 > x:
                right_ptr = median - 1
            else:
                left_ptr = median + 1
        return left_ptr