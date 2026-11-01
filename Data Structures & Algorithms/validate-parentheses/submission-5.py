class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for p in s:
            if p=='(' or p=='[' or p=='{':
                stack.append(p)           
            else:
                if len(stack)!=0:
                    pop = stack.pop()
                    if (pop=='(' and p!=')') or (pop=='[' and p!=']') or (pop=='{' and p!='}'):
                        return False
                else:
                     return False
        return len(stack)==0 