
#reference https://discuss.leetcode.com/topic/18942/python-solution-without-using-dictionary/2 
#Method 1: use a dictionary to map the original and the copy. O(n), space O(n)
# Definition for singly-linked list with a random pointer.
# class RandomListNode(object):
#     def __init__(self, x):
#         self.label = x
#         self.next = None
#         self.random = None

class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: RandomListNode
        :rtype: RandomListNode
        """
        if not head:
            return
        
        copy_map= {}
        node = head
        
        while node:
            new_node = RandomListNode(node.label)
            copy_map[node] = new_node
            node = node.next
            
        node = head
        while node:
            if node.next: 
                copy_map[node].next = copy_map[node.next]
            if node.random:
                copy_map[node].random = copy_map[node.random]
            node = node.next
            
        return copy_map[head]
        
  # method 2
  class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: RandomListNode
        :rtype: RandomListNode
        """
        if not head:
            return
        node = head
        while node:
            temp = node.next
            copy = RandomListNode(node.label)
            node.next = copy
            copy.next = temp
            node = node.next.next
            
        node = head
        while node:
            if node.random:
                node.next.random = node.random.next
            node = node.next.next
            
        new_head = head.next    
        node = head
        while node:
            if node.next:
                temp = node.next
                node.next = node.next.next
            if node.next:
                temp.next = node.next.next
            node = node.next
        return new_head
            
        
