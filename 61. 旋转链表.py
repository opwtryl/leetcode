'''
给定一个链表，旋转链表，将链表每个节点向右移动 k 个位置，其中 k 是非负数。

示例 1:

输入: 1->2->3->4->5->NULL, k = 2
输出: 4->5->1->2->3->NULL
解释:
向右旋转 1 步: 5->1->2->3->4->NULL
向右旋转 2 步: 4->5->1->2->3->NULL
示例 2:

输入: 0->1->2->NULL, k = 4
输出: 2->0->1->NULL
解释:
向右旋转 1 步: 2->0->1->NULL
向右旋转 2 步: 1->2->0->NULL
向右旋转 3 步: 0->1->2->NULL
向右旋转 4 步: 2->0->1->NULL
'''

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        # 计算链表长度
        tmp=head
        length=0
        while tmp:
            length+=1
            tmp=tmp.next
        # 长度为0 或者 旋转长度的整数倍都等价于不旋转    
        if length==0 or k%length==0  :return head
        
        
        result=head
        tmp=head
        cnt=length-k%length
        while cnt:
            # 旋转k次后，新的链尾
            if cnt==1:
                tmp.next,tmp=None,tmp.next
            else:
                tmp=tmp.next
            cnt-=1
        result=tmp# 新的链首
        
        # 原来的链尾要指向原来的链首
        while tmp:
            if tmp.next is None:
                tmp.next=head
                break
            tmp=tmp.next
            
        return result
            
        
        
