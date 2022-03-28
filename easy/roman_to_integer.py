class Solution:
    def romanToInt(self, s: str) -> int:
        number = 0
        romans = {
            'I':1,
            'V':5,
            'X':10,
            'L':50,
            'C':100,
            'D':500,
            'M':1000
        }
        prev_char = 'I'
        for char in s[::-1]:
            if romans[char]<romans[prev_char]:
                number -= romans[char]
            else:
                number += romans[char]
            prev_char = char
        return number