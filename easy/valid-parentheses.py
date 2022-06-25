class Solution:
    def isValid(self, s: str) -> bool:
        brackets_correspondence = {
            '}':'{',
            ')':'(',
            ']':'['
        }
        brackets_stack = []
        
        for bracket in s:
            if bracket not in brackets_correspondence.keys():
                brackets_stack.append(bracket)
            else:
                if brackets_stack:
                    opened_bracket = brackets_stack.pop()
                    if opened_bracket != brackets_correspondence[bracket]:
                        return False
                else: return False
        
        if brackets_stack:
            return False
        return True