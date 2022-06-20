class Solution:
    def hammingWeight(self, n:int) -> int:
        for i in range(5):
            m = int('0b' + ('0'*2**i + '1'*2**i)*2**(4-i), 2)
            n = (n&m) + ((n>>2**i)&m)
        return n