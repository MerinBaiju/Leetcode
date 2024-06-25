class Solution(object):
    def reverseVowels(self, s):
        sl=list(s)
        v=['a','e','i','o','u','A','E','I','O','U']
        i,j=0,len(sl)-1
        while i<j:
            while i<j and sl[i] not in v:
                i+=1
            while i<j and sl[j] not in v:
                j-=1
            sl[i],sl[j]=sl[j],sl[i]
            i+=1
            j-=1
        return ''.join(sl)    