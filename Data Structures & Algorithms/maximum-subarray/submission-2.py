# class Solution:
#     def maxSubArray(self, nums: List[int]) -> int:
#         if len(nums) == 1:
#             return nums[0]
        
#         global_max = float("-inf")
#         curSum = [float("-inf")] * (len(nums) + 1)
#         for idx, cur in enumerate(nums):
#             if curSum[idx] > 0: 
#                 curSum[idx+1] = curSum[idx] + cur
#             else: 
#                 curSum[idx+1] = cur
#             global_max = max(global_max, curSum[idx+1])
#         return global_max

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxSub, curSum = nums[0], 0
        for num in nums:
            if curSum < 0:
                curSum = 0
            curSum += num
            maxSub = max(maxSub, curSum)
        return maxSub