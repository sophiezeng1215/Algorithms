# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        stack = []
        lastVisited = None
        node = root
        vals = []
        while node or stack:
            if node:
                stack.append(node)
                node = node.left
            else:
                node = stack.pop()
                if node.right and node.right != lastVisited:
                    stack.append(node)
                    node = node.right
                else:
                    vals.append(node.val)
                    lastVisited = node
                    node = None
        return vals
