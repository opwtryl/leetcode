'''
给定一个包含非负整数的 m x n 网格，请找出一条从左上角到右下角的路径，使得路径上的数字总和为最小。

说明：每次只能向下或者向右移动一步。

示例:

输入:
[
  [1,3,1],
  [1,5,1],
  [4,2,1]
]
输出: 7
解释: 因为路径 1→3→1→1→1 的总和最小。
'''

class Solution:
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        '''
        状态转移方程：matrix[i][j]=min(matrix[i-1][j],matrix[i][j-1])+grid[i][j]
        边界：matrix[0][0]=grid[0][0]
        '''
        row=len(grid)
        if row==0:return 0
        col=len(grid[0])
        if col==0:return 0
        matrix=[[0 for n in range(col)] for m in range(row)]
        for i in range(row):
            for j in range(col):
                if i==0 and j==0:matrix[i][j]=grid[i][j]
                else:
                    top=matrix[i-1][j] if i!=0 else float('inf')
                    left=matrix[i][j-1] if j!=0 else float('inf')
                    matrix[i][j]=min(top,left)+grid[i][j]
        return matrix[row-1][col-1]
        
