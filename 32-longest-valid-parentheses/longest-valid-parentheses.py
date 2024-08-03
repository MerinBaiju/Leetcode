class Solution:
    def longestValidParentheses(self, s: str) -> int:
        o=0
        c=0
        a=0
        
        for i in s:
            if i=='(' :
                o+=1
            elif i==')':
                c+=1
            if c>o:
                o=0
                c=0
            elif(c==o):
                a=max(a,c*2)
        c=0
        o=0
        for i in s[::-1]:
            if i=='(' :
                o+=1
            elif i==')':
                c+=1
            if c<o:
                o=0
                c=0
            elif(c==o):
                a=max(a,c*2)
               
            
           

        print(o)
        print(c)
        print(a)
        return a