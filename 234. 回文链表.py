```
请判断一个链表是否为回文链表。

示例 1:

输入: 1->2
输出: false
示例 2:

输入: 1->2->2->1
输出: true
进阶：
你能否用 O(n) 时间复杂度和 O(1) 空间复杂度解决此题？
```
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# 时间复杂度：O(n)
# 空间复杂度：O(1)
class Solution:
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        
        
        # 计算长度
        length=0
        tmp1=head
        while tmp1:
            length+=1
            tmp1=tmp1.next
        
        # 反转前一半链表
        tmp=ListNode(0)
        for i in range(length//2):
           head.next,tmp.next,head=tmp.next,head,head.next
           
        # 如果长度为奇数，则从第(length+1)//2个开始对比
        if length%2==1:
            head=head.next
          
        # 一一对比反转的前一半链表和后一半链表的值，如果值不相等，则说明不是回文链表
        while head:
            if head.val!=tmp.next.val:
                return False
            head=head.next
            tmp=tmp.next
        
        return True
     
        
