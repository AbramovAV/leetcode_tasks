class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        ALPHABET = [chr(i) for i in range(ord('A'), ord('Z') + 1)]
        ALPHABET_LEN = 26
        title = ''
        while columnNumber:
            title = ALPHABET[(columnNumber-1) % ALPHABET_LEN] + title
            columnNumber = (columnNumber-1) // ALPHABET_LEN
        return title