class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        parenthesis = {")" : "(" ,"}":"{" ,"]":"["}
        for p in s:
            if p in parenthesis.values():
                stack.append(p)
            elif stack and parenthesis[p] == stack[-1]:
                stack.pop()
            else:
                return False
        return stack == []
