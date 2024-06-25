class Solution(object):
    def reverseWords(self, s):
        r=s.split()
        return ' '.join(r[::-1])


        