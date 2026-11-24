# class Solution:
#     def canJump(self, nums: List[int]) -> bool:
#         n = len(nums)
#         visit = [-1] * n

#         def dfs(idx):
#             if visit[idx] != -1:
#                 return visit[idx]

#             if idx >= n - 1:
#                 return True
#             for step in range(1, nums[idx] + 1):
#                 res = dfs(idx + step)
#                 visit[idx + step] = res
#                 if res:
#                     return True
#             return False

#         return dfs(0)

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        goal = n - 1

        for idx in range(n-2, -1, -1):
            if nums[idx] + idx >= goal:
                goal = idx 
        
        return goal == 0