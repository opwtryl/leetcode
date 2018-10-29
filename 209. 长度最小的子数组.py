'''
给定一个含有 n 个正整数的数组和一个正整数 s ，找出该数组中满足其和 ≥ s 的长度最小的连续子数组。如果不存在符合条件的连续子数组，返回 0。

示例: 

输入: s = 7, nums = [2,3,1,2,4,3]
输出: 2
解释: 子数组 [4,3] 是该条件下的长度最小的连续子数组。
进阶:

如果你已经完成了O(n) 时间复杂度的解法, 请尝试 O(n log n) 时间复杂度的解法。
'''
# 时间复杂度：O(n)
# 空间复杂度：O(1)

class Solution:
    def minSubArrayLen(self, s, nums):
        """
        :type s: int
        :type nums: List[int]
        :rtype: int
        """
        slow=0
        fast=0
        sumSubNums=0
        lenSubNums=float('inf')
        while  fast<len(nums):
            sumSubNums+=nums[fast]

            while sumSubNums>=s:
                slow,fast,sumSubNums
                lenSubNums=min(lenSubNums,fast-slow+1)
                lenSubNums
                sumSubNums-=nums[slow]
                slow+=1

            fast+=1
        return 0 if lenSubNums==float('inf') else lenSubNums
        
