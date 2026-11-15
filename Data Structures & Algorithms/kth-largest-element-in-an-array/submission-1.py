class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # heapq.heapify_max(nums)

        # for _ in range(k):
        #     res = heapq.heappop_max(nums)
        # return res

        heap = nums[:k]
        heapq.heapify(heap)
        for n in nums[k:]:
            if n > heap[0]:
                heapq.heapreplace(heap, n)
        return heap[0]