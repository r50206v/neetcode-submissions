class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        ans = []
        path = []

        # def dfs(idx):
        #     total = sum(path)
        #     if total == target:
        #         ans.append(path[:])
        #         return 
        #     elif total > target:
        #         return 
        #     elif idx == len(nums):
        #         return

        #     path.append(nums[idx])
        #     dfs(idx)
        #     path.pop()
        #     dfs(idx + 1)
        
        # dfs(0)
        # return ans
        def dfs(idx, remain):
            if remain == 0:
                ans.append(path[:])
                return
            if remain < 0 or idx == len(nums):
                return
            path.append(nums[idx])
            dfs(idx, remain - nums[idx])
            path.pop()
            dfs(idx + 1, remain)
        dfs(0, target)
        return ans