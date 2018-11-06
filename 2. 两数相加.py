'''
给定两个非空链表来表示两个非负整数。位数按照逆序方式存储，它们的每个节点只存储单个数字。将两数相加返回一个新的链表。

你可以假设除了数字 0 之外，这两个数字都不会以零开头。

示例：

输入：(2 -> 4 -> 3) + (5 -> 6 -> 4)
输出：7 -> 0 -> 8
原因：342 + 465 = 807
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        head=ListNode((l1.val+l2.val)%10)
        quotient=(l1.val+l2.val)//10
        tmp=head
        l1=l1.next
        l2=l2.next
        
        while l1 or l2 or quotient:
            val1=l1.val if l1 else 0
            val2=l2.val if l2 else 0
            sumVal=val1+val2+quotient
            nextVal=sumVal%10
            quotient=sumVal//10
            tmp.next=ListNode(nextVal)
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
            tmp=tmp.next
            
        return head
        
        
