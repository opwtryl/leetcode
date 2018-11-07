'''
给定正整数 n，找到若干个完全平方数（比如 1, 4, 9, 16, ...）使得它们的和等于 n。你需要让组成和的完全平方数的个数最少。

示例 1:

输入: n = 12
输出: 3 
解释: 12 = 4 + 4 + 4.
示例 2:

输入: n = 13
输出: 2
解释: 13 = 4 + 9.
'''

class Solution:
    
    '''
    利用类变量就不会超时，利用局部变量就会超时。
    因为类变量会被修改而重复利用。如：
    In:     Solution().numSquares(10)# 计算10次
    Out:    2
    In:     Solution()._num
    Out:    [0, 1, 2, 3, 1, 2, 3, 4, 2, 1, 2]
    In:     Solution().numSquares(20)# 只需要计算10次，而不是20次
    Out:    2
    In:     Solution()._num
    Out:    [0, 1, 2, 3, 1, 2, 3, 4, 2, 1, 2, 3, 3, 2, 3, 4, 1, 2, 2, 3, 2]
    
    '''
    _num = [0]
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        num = self._num 
        while len(num) <= n:
            num += min(num[-i*i] for i in range(1, int(len(num)**0.5+1))) + 1,
        return num[n]
                
                
            
        
