class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        stats = {x:0 for x in range (1,33)}
        for num in nums:
            num = bin(num)[2:]
            for i in range(1, len(num)+1):
                if num[-i] == '1':
                    stats[i] += 1
        
        mode = ''
        majority_criteria = len(nums)//2
        for i in range(32, 0, -1):
            if stats[i] > majority_criteria:
                mode = mode + "1"
            else:
                mode = mode + "0"
        return int(mode, 2)