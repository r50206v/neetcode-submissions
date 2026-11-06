# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        def dfs(node, floor, ceil):
            if not node:
                return True

            if not (floor < node.val < ceil):
                return False
            
            return dfs(node.left, floor, node.val) &\
                    dfs(node.right, node.val, ceil)
            # cond = True & (floor < node.val < ceil)
            # if node.left:
            #     cond = cond & (node.left.val < node.val)
            # if node.right:
            #     cond = cond & (node.right.val > node.val)

            # return cond &\
            #        dfs(node.left, floor, node.val) &\
            #        dfs(node.right, node.val, ceil)
        
        return dfs(root, float("-inf"), float("inf"))
        
