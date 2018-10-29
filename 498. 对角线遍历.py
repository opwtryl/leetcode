'''
给定一个含有 M x N 个元素的矩阵（M 行，N 列），请以对角线遍历的顺序返回这个矩阵中的所有元素，对角线遍历如下图所示。

 

示例:

输入:
[
 [ 1, 2, 3 ],
 [ 4, 5, 6 ],
 [ 7, 8, 9 ]
]

输出:  [1,2,4,7,5,3,6,8,9]

解释:

 

说明:

给定矩阵中的元素总数不会超过 100000 。
'''

class Solution:
    def findDiagonalOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        
        m=len(matrix)
        if m==0:return []
        
        n=len(matrix[0])
        if n==0:return []
        
        result=[]
        i=0
        j=0
        # 利用对角线索引 i+j=x
        for x in range(m+n-1):
        
            # x为偶数，向右上遍历
            if x%2==0:
                i=min(x,m-1)
                j=x-i
                while j<n and i>=0:
                    result.append(matrix[i][j])
                    i-=1
                    j+=1
                    
            # x为奇数，向左下遍历
            else:
                j=min(x,n-1)
                i=x-j
                while i<m and j>=0:
                    result.append(matrix[i][j])
                    i+=1
                    j-=1

        return result
