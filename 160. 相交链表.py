'''
编写一个程序，找到两个单链表相交的起始节点。

 

例如，下面的两个链表：

A:          a1 → a2
                   ↘
                     c1 → c2 → c3
                   ↗            
B:     b1 → b2 → b3
在节点 c1 开始相交。

 

注意：

如果两个链表没有交点，返回 null.
在返回结果后，两个链表仍须保持原有的结构。
可假定整个链表结构中没有循环。
程序尽量满足 O(n) 时间复杂度，且仅用 O(1) 内存。
'''

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        lenA=0
        lenB=0
        
        #计算A链表的长度
        tmp=headA
        while tmp:
            lenA+=1
            tmp=tmp.next
            
        #计算B链表的长度
        tmp=headB
        while tmp:
            lenB+=1
            tmp=tmp.next
        
        #链表长度差
        diff=lenA-lenB
        
        tmp1=headA if diff>0 else headB
        tmp2=headB if diff>0 else headA
        
        #遍历到两链表长度相同的位置
        diff=abs(diff)
        while diff:
            tmp1=tmp1.next
            diff-=1
            
        #从链表长度相同的位置开始遍历，相遇点则为交叉点
        while tmp1:
            if tmp1 is tmp2:
                return tmp1
            else:
                tmp1=tmp1.next
                tmp2=tmp2.next
                
        return None
        
            
        
            
