# 给定一个链表，判断链表中是否有环。

# 进阶：
# 你能否不使用额外空间解决此题？
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None
#时间复杂度：O(n)
#空间复杂度：O(1)
class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        # 两个不同速度的指针遍历，如果存在环形，则总会相遇
        slow=head
        fast=head
        if head is None:
            return False
        while True:
            slow=slow.next
            
            try:
                fast=fast.next.next
            # fast is None OR fast.next is None,说明不是环形
            except:
                return False
            # 相遇说明是环形
            if slow==fast:
                return True
