class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        matchingMap = {
            target-nums[idx]: idx for idx in range(len(nums))
        }

        for jdx in range(len(nums)):
            if matchingMap.get(nums[jdx]) and matchingMap.get(nums[jdx]) != jdx:
                return sorted([matchingMap.get(nums[jdx]), jdx])
        
        return []