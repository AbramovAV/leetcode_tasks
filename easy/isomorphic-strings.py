class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        mapping_s = {}
        mapping_t = {}
        for char_s, char_t in zip(s,t):
            if char_s not in mapping_s and char_t not in mapping_t:
                mapping_s[char_s] = char_t
                mapping_t[char_t] = char_s
            elif char_s in mapping_s and char_t in mapping_t and \
                mapping_s[char_s] == char_t and mapping_t[char_t] == char_s:
                continue
            else:
                return False
        return True