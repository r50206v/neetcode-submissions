class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # if len(nums) == 0: 
        #     return 0
        
        # heapq.heapify(nums)
        # heap = nums
        # ans = 0

        # start = heapq.heappop(heap)
        # tmp_ans = 1
        # while len(heap) > 0:
        #     nxt = heapq.heappop(heap)
        #     if start + 1 == nxt:
        #         tmp_ans += 1
        #     elif start == nxt:
        #         continue
        #     else:
        #         ans = max(ans, tmp_ans)
        #         tmp_ans = 1
        #     start = nxt
        # return max(ans, tmp_ans)

        
        numSet = set(nums)
        ans = 0
        for n in nums:
            if n - 1 not in numSet:
                length = 0
                while n + length in numSet:
                    length += 1
                ans = max(ans, length)
        return ans
