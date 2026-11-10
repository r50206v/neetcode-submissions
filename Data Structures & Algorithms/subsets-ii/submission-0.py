class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        ans = [[]]
        path = []
        nums.sort()

        def dfs(idx):
            if idx == len(nums):
                if path not in ans: ans.append(path[:])
                return 
            
            path.append(nums[idx])
            if path not in ans:
                ans.append(path[:])
            dfs(idx + 1)

            path.pop()
            dfs(idx + 1)
        
        dfs(0)
        return ans