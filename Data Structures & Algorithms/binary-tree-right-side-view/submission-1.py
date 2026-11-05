# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        ans = []

        if not root:
            return ans

        q = collections.deque()
        q.append(root)

        while q:
            qLen = len(q)
            level = collections.deque()
            for idx in range(qLen):
                node = q.popleft()
                if node.left: level.append(node.left)
                if node.right: level.append(node.right)
                
                if idx == qLen - 1:
                    ans.append(node.val)
            q = level
            
        return ans
