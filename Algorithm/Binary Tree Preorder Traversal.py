#Time O(n), space O(n)
#append node.val, use a stack to store node.right(only), and then move node to the left, and 

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if root == []:
            return 
        stack = []
        vals = []
        node = root
        while stack or node:
            if node:
                vals.append(node.val)
                stack.append(node.right)
                node = node.left
            else:
                node = stack.pop()
        return vals
