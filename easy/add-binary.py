class Solution:
    def addBinary(self, a: str, b: str) -> str:
        res = ''
        overflow = 0
        sum = 0
        i, j = len(a)-1, len(b) - 1
        while i>=0 or j>=0:
            sum = overflow
            if i>=0: sum += ord(a[i]) - ord('0')
            if j>=0: sum += ord(b[j]) - ord('0')
            overflow = sum // 2
            res = str(sum % 2) + res
            i, j = i-1, j-1
        if overflow: res = '1' + res
        return  res