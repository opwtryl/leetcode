'''
给定一个由 '1'（陆地）和 '0'（水）组成的的二维网格，计算岛屿的数量。一个岛被水包围，并且它是通过水平方向或垂直方向上相邻的陆地连接而成的。你可以假设网格的四个边均被水包围。

示例 1:

输入:
11110
11010
11000
00000

输出: 1
示例 2:

输入:
11000
11000
00100
00011

输出: 3
'''
class Solution:
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        if len(grid)==0:return 0
        if len(grid[0])==0:return 0
        row=len(grid)
        col=len(grid[0])
        cnt=0
        for i in range(row):
            for j in range(col):
                if grid[i][j]=='1':
                    self.dfs(grid,row,col,i,j)
                    cnt+=1
        return cnt
        
    def dfs(self,grid,row,col,i,j):
        if grid[i][j]=='0':return
        grid[i][j]='0' # 把‘1’改为‘0’
        
        # 把‘1’上下左右的‘1’都改为‘0’
        if i!=0:self.dfs(grid,row,col,i-1,j)
        if i!=row-1:self.dfs(grid,row,col,i+1,j)
        if j!=0:self.dfs(grid,row,col,i,j-1)
        if j!=col-1:self.dfs(grid,row,col,i,j+1)
            
