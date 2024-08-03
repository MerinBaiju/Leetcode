class Solution:
    def isValid(self, s: str) -> bool:
        l=[]
        p={
            '(':')',
            '{':'}',
            '[':']'
        }
        for i in s:
            if i in p:
                l.append(i)
            elif len(l)==0 or i!=p[l.pop()]:
                return False
        return len(l)==0

            
        