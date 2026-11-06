# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        self.ans = 0

        def dfs(node, max_parent):
            if not node:
                return None
            
            if node.val >= max_parent:
                print(node.val)
                self.ans += 1
            
            max_parent = max(max_parent, node.val)
            dfs(node.left, max_parent)
            dfs(node.right, max_parent)
        
        dfs(root, float("-inf"))
        return self.ans