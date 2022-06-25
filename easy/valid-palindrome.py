class Solution:
    def isPalindrome(self, s: str) -> bool:
        left_ptr = 0
        right_ptr = len(s) - 1
        while left_ptr <= right_ptr:
            if s[left_ptr].isalnum() and \
                s[right_ptr].isalnum():
                if s[left_ptr].lower() != s[right_ptr].lower():
                    return False
                else:
                    left_ptr += 1
                    right_ptr -= 1
            elif not s[left_ptr].isalnum():
                left_ptr += 1
            else:
                right_ptr -= 1
        return True