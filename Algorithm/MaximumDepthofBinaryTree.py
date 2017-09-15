# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# recursive
class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        else:
            return max(self.maxDepth(root.left), self.maxDepth(root.right)) + 1
            
# level traversal
class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        import Queue
        q = Queue.Queue()
        q.put(root)
        curNum = 1
        nextNum = 0
        level = 0
        while (not q.empty()):
            node = q.get()
            if node.left:
                q.put(node.left)
                nextNum += 1
            if node.right:
                q.put(node.right)
                nextNum += 1
            curNum -= 1
            if curNum == 0:
                level += 1
                curNum = nextNum
                nextNum = 0
        return level
