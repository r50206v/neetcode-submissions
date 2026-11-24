class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        visit = [-1] * n

        def dfs(idx):
            if idx >= n - 1:
                return True
            if visit[idx] != -1:
                return visit[idx]
            for step in range(1, nums[idx] + 1):
                if dfs(idx + step):
                    visit[idx] = True
                    return True
            visit[idx] = False
            return False

        return dfs(0)

# class Solution:
#     def canJump(self, nums: List[int]) -> bool:
#         n = len(nums)
#         goal = n - 1
#         for idx in range(n-2, -1, -1):
#             if nums[idx] + idx >= goal:
#                 goal = idx 
        
#         return goal == 0