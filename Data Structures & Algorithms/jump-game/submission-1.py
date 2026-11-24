from functools import cache

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)

        @cache
        def dfs(idx):
            if idx >= n - 1:
                return True
            for step in range(1, nums[idx] + 1):
                if dfs(idx + step):
                    return True
            return False

        return dfs(0)