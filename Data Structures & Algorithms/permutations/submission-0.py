class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        def dfs():
            if len(path) == len(nums):
                ans.append(path[:])
                return 

            for x in nums:
                if x in path:
                    continue
                path.append(x)
                dfs()
                path.pop()

        ans = []
        path = []
        dfs()
        return ans