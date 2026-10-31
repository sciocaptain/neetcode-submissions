class Solution:
    def isValid(self, s: str) -> bool:
        
        d = {")": "(", "}": "{", "]": "["}        
        stack = []

        for c in s:
            if c in d and stack:    
                if stack.pop() == d[c]:
                    continue
                else:
                    return False
            else:
                stack.append(c)
        return len(stack) == 0