# DFS. Process node, push it to stack, get its neighbors, copy each neighbor, push each neighbor to stack

# Definition for a undirected graph node
# class UndirectedGraphNode:
#     def __init__(self, x):
#         self.label = x
#         self.neighbors = []

class Solution:
    # @param node, a undirected graph node
    # @return a undirected graph node
    def cloneGraph(self, node):
        if not node:
            return
        stack = []
        c_head = UndirectedGraphNode(node.label)
        c_map = {node:c_head}
        stack.append(node)
        
        while stack:
            node = stack.pop()
            for neighbor in node.neighbors:
                if neighbor not in c_map:
                    c_neighbor = UndirectedGraphNode(neighbor.label)
                    c_map[neighbor] = c_neighbor
                    stack.append(neighbor)
                c_map[node].neighbors.append(c_map[neighbor])
        return c_head
  
  # DFS. Use collections.deque
  
  class Solution:
    # @param node, a undirected graph node
    # @return a undirected graph node
    def cloneGraph(self, node):
        if not node:
            return
        
        c_head = UndirectedGraphNode(node.label)
        c_map = {node:c_head}
        queue = collections.deque([node])
        
        while queue:
            node = queue.popleft()
            for neighbor in node.neighbors:
                if neighbor not in c_map:
                    c_neighbor = UndirectedGraphNode(neighbor.label)
                    c_map[neighbor] = c_neighbor
                    queue.append(neighbor)
                c_map[node].neighbors.append(c_map[neighbor])
        return c_head
