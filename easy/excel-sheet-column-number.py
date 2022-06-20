class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        number = 0
        for idx, symbol in enumerate(columnTitle[::-1]):
            number += (ord(symbol) - ord('A') + 1) * 26**idx
        return number