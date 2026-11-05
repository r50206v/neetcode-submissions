# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        # ans = []

        # if not root:
        #     return ans

        # q = collections.deque()
        # q.append(root)

        # while q:
        #     qLen = len(q)
        #     for idx in range(qLen):
        #         node = q.popleft()
        #         if node.left: q.append(node.left)
        #         if node.right: q.append(node.right)
                
        #     if node:
        #         ans.append(node.val)
            
        # return ans

        res = []


        def dfs(node, depth):
            if not node:
                return None
            if depth == len(res):
                res.append(node.val)
            
            dfs(node.right, depth + 1)
            dfs(node.left, depth + 1)
        
        dfs(root, 0)
        return res
