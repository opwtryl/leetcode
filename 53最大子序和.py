'''
给定一个整数数组 nums ，找到一个具有最大和的连续子数组（子数组最少包含一个元素），返回其最大和。

示例:

输入: [-2,1,-3,4,-1,2,1,-5,4],
输出: 6
解释: 连续子数组 [4,-1,2,1] 的和最大，为 6。
'''
# 时间复杂度：O(n)
# 空间复杂度：O(1)
class Solution:
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_subarray=float('-inf')
        sum_subarray=0
        for num in nums:
            if sum_subarray<=0:
                sum_subarray=num  # 前面的序列和小于等于0，则重新开始
            else:
                sum_subarray+=num
            max_subarray=max(max_subarray,sum_subarray)
        return max_subarray
        
