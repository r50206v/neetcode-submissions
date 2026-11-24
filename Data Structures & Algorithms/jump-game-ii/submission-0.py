class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        visit = [-1] * n

        def dfs(idx): 
            if idx >= n - 1:
                return 0
            if visit[idx] >= 0:
                return visit[idx]
            
            min_jump = float("inf")
            for step in range(nums[idx], 0, -1):
                min_jump = min(min_jump, dfs(idx + step))
            
            visit[idx] = min_jump + 1
            return visit[idx]

        return dfs(0)
