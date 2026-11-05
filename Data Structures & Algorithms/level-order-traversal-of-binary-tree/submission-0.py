# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        ans = []

        if not root:
            return ans

        level = [root]
        while level: 
            ans.append([n.val for n in level])
            next_level = []
            for n in level:
                if n.left: next_level.append(n.left)
                if n.right: next_level.append(n.right)
            level = next_level
        return ans