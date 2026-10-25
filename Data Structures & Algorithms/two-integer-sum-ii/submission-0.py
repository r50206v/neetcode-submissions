class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        
        left = 0
        right = len(numbers) - 1

        while numbers[left] + numbers[right] != target:
            if numbers[left] + numbers[right] > target:
                right -= 1
            elif numbers[left] + numbers[right] < target: 
                left += 1
            
        return [left + 1, right + 1]

        # for idx in range(len(numbers)):

        #     for jdx in range(idx, len(numbers)):

        #         if numbers[idx] + numbers[jdx] == target:
        #             return [idx + 1, jdx + 1]