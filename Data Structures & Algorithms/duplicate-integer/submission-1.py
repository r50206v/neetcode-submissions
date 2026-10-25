class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        if len(nums) == 0:
            return False

        checkSet = set([])
        for idx in range(len(nums)):
            if nums[idx] not in checkSet:
                checkSet.add(nums[idx])
            else:
                return True
        
        return False
