'''
您将获得一个双向链表，除了下一个和前一个指针之外，它还有一个子指针，可能指向单独的双向链表。这些子列表可能有一个或多个自己的子项，依此类推，生成多级数据结构，如下面的示例所示。

扁平化列表，使所有结点出现在单级双链表中。您将获得列表第一级的头部。

 

示例:

输入:
 1---2---3---4---5---6--NULL
         |
         7---8---9---10--NULL
             |
             11--12--NULL

输出:
1-2-3-7-8-11-12-9-10-4-5-6-NULL
'''

"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""
class Solution(object):
    def flatten(self, head):
        """
        :type head: Node
        :rtype: Node
        """
        stack=[] #存储父节点
        tmp=head
        while tmp:
        
            if tmp.child is not None:# 添加父节点
                stack.append(tmp)
                tmp=tmp.child
                
            elif tmp.next is None:遍历到了链尾
                if stack:#遍历到了链尾，但有父节点
                    parent=stack.pop()# 取出最近的父节点
                    
                    if parent.next is None:# 如果父节点也为链尾
                        parent.next,parent.child.prev,parent.child=parent.child,parent,None
                        
                    else:# 如果父节点不为链尾
                        tmp.next,parent.next.prev=parent.next,tmp
                        parent.next,parent.child.prev,parent.child=parent.child,parent,None
                        tmp=tmp.next
                
                else:#遍历到了链尾，但没有父节点
                    return head
            else:# 无子节点且非链尾的节点
                tmp=tmp.next
