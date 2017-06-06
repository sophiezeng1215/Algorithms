#Method 1: recursive call; "report" to the parent whether p or q or find. Space O(n) - worse case for unbalanced tree and O(lgn) for balanced tree, time O(n)

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        if not root or root == p or root == q:
            return root
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)
        if left and right:
            return root
        elif left:
            return left
        else:
            return right


# Method 2: use a stack and post-order traversal to find paths of p and q

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        p_path = self.findPath(root, p)
        q_path = self.findPath(root, q)
        res = None
        i = 0
        while i < min(len(p_path), len(q_path)) and p_path[i] == q_path[i]:
            res = p_path[i]
            i += 1
        return res
        
    def findPath(sef, root, p):
        stack = []
        lastVisited = None
        node = root
        while node or stack:
            if node:
                stack.append(node)
                node = node.left
            else:
                node = stack[-1]
                if node.right and node.right != lastVisited:
                    node = node.right
                else:
                    if node == p:
                        return stack
                    lastVisited = stack.pop()
                    node = None
        return stack
