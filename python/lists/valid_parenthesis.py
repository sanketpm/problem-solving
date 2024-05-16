from collections import deque

class Solution:
    def isValid(self, s: str) -> bool:
        openBrace = {}
        openBrace[')'] = '('
        openBrace['}'] = '{'
        openBrace[']'] = '['

        stk = deque()

        for brace in s:
            if brace in ['(', '{', '[']:
                stk.append(brace)
            elif not stk or stk.pop() != openBrace[brace]:
                return False 
        
        return False if stk else True

print(Solution().isValid("()[]{}"))