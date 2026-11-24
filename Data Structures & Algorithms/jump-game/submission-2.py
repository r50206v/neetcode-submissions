# from functools import cache

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        visit = [-1] * n

        # @cache
        def dfs(idx):
            if visit[idx] != -1:
                return visit[idx]

            if idx >= n - 1:
                return True
            for step in range(1, nums[idx] + 1):
                res = dfs(idx + step)
                visit[idx + step] = res
                if res:
                    return True
            return False

        return dfs(0)