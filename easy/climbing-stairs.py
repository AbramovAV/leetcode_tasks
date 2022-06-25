class Solution:
    def climbStairs(self, n: int) -> int:
        start, num_climbs = 0, 1
        for i in range(n):
            start, num_climbs = num_climbs, start + num_climbs
        return num_climbs