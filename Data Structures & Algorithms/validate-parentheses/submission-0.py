class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        reference = {")":"(","]":"[","}":"{"}
        
        for bracket in s:
            if bracket in reference:
                if stack and stack[-1] == reference[bracket]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(bracket)
        
        return True if not stack else False