class Solution:
    def reverseBits(self, n: int) -> int:
        reversed_n = 0
        current_digit = 31
        while n>0:
            mod = n%2
            n = n//2
            reversed_n += mod * (2**current_digit)
            current_digit -= 1
        return reversed_n