class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        # ans = [[]]
        # for x in nums:
        #     ans += [s + [x] for s in ans]
        # return ans

        ans = []
        path = []

        def dfs(i):
            if i == len(nums):          # decided on every element
                print(path)
                ans.append(path[:])     # save a COPY
                return

            path.append(nums[i])        # choice 1: include nums[i]
            dfs(i + 1)
            path.pop()                  # undo, so the next branch starts clean

            dfs(i + 1)                  # choice 2: exclude nums[i]

        dfs(0)
        return ans