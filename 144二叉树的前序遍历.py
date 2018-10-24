'''
给定一个二叉树，返回它的 前序 遍历。

 示例:

输入: [1,null,2,3]  
   1
    \
     2
    /
   3 

输出: [1,2,3]
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        # 递归算法
        # if root is not None:
        #     return [root.val]+self.preorderTraversal(root.left)+self.preorderTraversal(root.right)
        # return []
        
        # 迭代算法
        result=[]
        stack=[root]
        while stack:
            node=stack.pop()
            if node:
                result.append(node.val)
                if node.right:
                    stack.append(node.right)
                if node.left:
                    stack.append(node.left)
        return result
        
