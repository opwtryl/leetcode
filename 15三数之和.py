'''
给定一个包含 n 个整数的数组 nums，判断 nums 中是否存在三个元素 a，b，c ，使得 a + b + c = 0 ？找出所有满足条件且不重复的三元组。

注意：答案中不可以包含重复的三元组。

例如, 给定数组 nums = [-1, 0, 1, 2, -1, -4]，

满足要求的三元组集合为：
[
  [-1, 0, 1],
  [-1, -1, 2]
]
'''
# 时间复杂度：O(n^2)
# 空间复杂度：O(1)
class Solution:
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if len(nums)<3:
            return []
        
        nums.sort() # 从小到大排列
        last=float('-inf')
        length=len(nums)
        result=[]
        for i in range(length-2):
        
            if nums[i]>0:# 遍历到正数则跳出循环
                return result
            elif nums[i]!=last :# 跳过重复项

                left=i+1
                right=length-1
                while left<right:
                    if nums[left]+nums[right]+nums[i]<0:
                        left+=1
                    elif nums[left]+nums[right]+nums[i]>0:
                        right-=1
                    else:
                        result.append([nums[i],nums[left],nums[right]])
                        while left<right and nums[left]==nums[left+1]:
                            left+=1
                        while left<right and nums[right]==nums[right-1]:
                            right-=1
                        left+=1
                        right-=1
            last=nums[i]
        return result
