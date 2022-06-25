class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = strs[0]
        for string in strs[1:]:
            sub_prefix = ''
            for pref_c, str_c in zip(prefix, string):
                if pref_c == str_c:
                    sub_prefix += pref_c
                else:
                    break
            prefix = sub_prefix
        return prefix