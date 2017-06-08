#Use "prev" and 'temp' = node.next; return prev
#Time O(n), space O(1)

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        node = head
        prev = None
        while node:
            temp = node.next
            node.next = prev
            prev = node
            node = temp
        return prev
