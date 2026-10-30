class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ans = []
        nums = sorted(nums)

        for idx in range(len(nums)):
            if idx > 0 and nums[idx] == nums[idx - 1]:
                continue  # skip duplicate anchors
            if nums[idx] > 0:
                break     # sorted, so no way to sum to 0 from here

            left = idx + 1
            right = len(nums) - 1
            while left < right:
                if nums[left] + nums[right] < -1*nums[idx]:
                    left += 1
                elif nums[left] + nums[right] > -1*nums[idx]:
                    right -= 1
                else: 
                    ans.append([nums[left], nums[right], nums[idx]])
                    left += 1
                    right -= 1
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1  # skip duplicate lefts
        return ans
                