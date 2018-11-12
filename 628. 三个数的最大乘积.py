'''
给定一个整型数组，在数组中找出由三个数组成的最大乘积，并输出这个乘积。

示例 1:

输入: [1,2,3]
输出: 6
示例 2:

输入: [1,2,3,4]
输出: 24
注意:

给定的整型数组长度范围是[3,104]，数组中所有的元素范围是[-1000, 1000]。
输入的数组中任意三个数的乘积不会超出32位有符号整数的范围。
'''
class Solution:
    def maximumProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        '''
        nums从小到大排序
        全部num都是正：后三个数字乘积最大
        只有一个num是负：后三个数字乘积最大
        有两个num是负：后三个数字乘积和前两个负数与最后一个数字乘积间的最大值
        有3个num是负：后三个数字乘积和前两个负数与最后一个数字乘积间的最大值
        全部num都是负：后三个数字乘积最大
        '''
        nums.sort()
        return max(nums[0]*nums[1]*nums[-1],nums[-1]*nums[-2]*nums[-3])
