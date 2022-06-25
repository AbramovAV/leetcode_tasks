class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        length = 0
        seen_symbol = False
        for i in range(len(s)-1,-1,-1):
            if s[i] != ' ':
                seen_symbol = True or seen_symbol
                length += 1
            elif seen_symbol:
                break
            else:
                continue
        return length