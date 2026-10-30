class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0: 
            return 0
        
        heapq.heapify(nums)
        heap = nums
        ans = 0

        start = heapq.heappop(heap)
        tmp_ans = 1
        while len(heap) > 0:
            nxt = heapq.heappop(heap)
            if start + 1 == nxt:
                tmp_ans += 1
            elif start == nxt:
                continue
            else:
                ans = max(ans, tmp_ans)
                tmp_ans = 1
            start = nxt
        return max(ans, tmp_ans)

        # min_val = min(nums)
        # max_val = max(nums)

        # hash = set(nums)
        # ans = 0
        # tmp_ans = 0
        # for n in range(min_val, max_val+1):
        #     print(n, ans, tmp_ans)
        #     if n-1 not in hash:
        #         tmp_ans = 1
        #         continue
        #     else: 
        #         tmp_ans += 1
        #         ans = max(ans, tmp_ans)
        # return ans