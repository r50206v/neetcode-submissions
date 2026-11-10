# class Solution:
#     def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
#         ans = [[]]
#         path = []
#         nums.sort()

#         def dfs(idx):
#             if idx == len(nums):
#                 if path not in ans: ans.append(path[:])
#                 return 
            
#             path.append(nums[idx])
#             if path not in ans:
#                 ans.append(path[:])
#             dfs(idx + 1)

#             path.pop()
#             dfs(idx + 1)
        
#         dfs(0)
#         return ans


class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()

        def backtrack(i, subset):
            if i == len(nums):
                res.append(subset[::])
                return

            subset.append(nums[i])
            backtrack(i + 1, subset)
            subset.pop()

            while i + 1 < len(nums) and nums[i] == nums[i + 1]:
                i += 1
            backtrack(i + 1, subset)

        backtrack(0, [])
        return res