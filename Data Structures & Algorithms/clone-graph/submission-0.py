"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        hashmap = defaultdict(list)
        if not node:
            return node
        
        curr = node
        idx = 1
        while curr.val not in hashmap:
            hashmap[idx] = Node(curr.val)
            hashmap[idx].neighbors = [n.val for n in curr.neighbors]

            for next_node in curr.neighbors:
                if next_node.val not in hashmap:
                    curr = next_node
                    idx = next_node.val
                    break
        
        idx = 1
        while idx <= len(list(hashmap.keys())):
            curr = hashmap[idx]
            curr.neighbors = [hashmap[n_val] for n_val in curr.neighbors]
            idx += 1
        
        return hashmap[1]