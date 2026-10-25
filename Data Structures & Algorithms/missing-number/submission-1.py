class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        # seen = set(nums)

        # for i in range(len(nums) + 1):
        #     if i in seen:
        #         continue
        #     else: 
        #         return i
        
        # return None

        n = len(nums)
        xorr = n
        for i in range(n):
            xorr = i ^ nums[i] ^ xorr
        return xorr
