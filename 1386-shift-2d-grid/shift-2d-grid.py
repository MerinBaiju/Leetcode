class Solution(object):
    def shiftGrid(self, grid, k):
        m,n=len(grid),len(grid[0])
        res=[[0]*n for i in range(m)]
        for i in range(m):
            for j in range(n):
                one=((i*n+j)+k)%(m*n)
                nr,nc=one//n,one%n
                res[nr][nc]=grid[i][j]
        return res
        