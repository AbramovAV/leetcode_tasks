class Solution:
    def isHappy(self, n: int) -> bool:
        seen_sums = set()
        while True:
            sum = 0
            while n>0:
                sum += (n%10)**2
                n //= 10
            if sum == 1: return True
            elif sum in seen_sums: return False
            seen_sums.add(sum)
            n = sum