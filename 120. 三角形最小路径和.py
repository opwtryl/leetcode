'''
给定一个三角形，找出自顶向下的最小路径和。每一步只能移动到下一行中相邻的结点上。

例如，给定三角形：

[
     [2],
    [3,4],
   [6,5,7],
  [4,1,8,3]
]
自顶向下的最小路径和为 11（即，2 + 3 + 5 + 1 = 11）。

说明：

如果你可以只使用 O(n) 的额外空间（n 为三角形的总行数）来解决这个问题，那么你的算法会很加分。
'''
class Solution:
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        
        '''
        状态转移方程：minPaths[i]=min(minPaths[i],minPaths[i-1])+t[i]
        边界：minPaths[0]=0,minPaths[1:]=float('inf')
        '''
        if triangle==[]:return 0
        
        n=len(triangle)
        minPaths=[float('inf')]*n
        minPaths[0]=0
        for t in triangle :
            for i in range(len(t)-1,-1,-1):
                tmp=float('inf') if i==0  else minPaths[i-1]
                minPaths[i]=min(minPaths[i],tmp)+t[i]
        return min(minPaths)
