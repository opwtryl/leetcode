'''
删除链表中等于给定值 val 的所有节点。

示例:

输入: 1->2->6->3->4->5->6, val = 6
输出: 1->2->3->4->5
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        while head and head.val==val:
            head=head.next
            
        h=head
        tmp=ListNode(0)
        
        while h:
            
            if h.val==val:
                h.next,tmp.next.next,h=None,h.next,h.next
            else:
                h,tmp.next=h.next,h
        return head
            
        
