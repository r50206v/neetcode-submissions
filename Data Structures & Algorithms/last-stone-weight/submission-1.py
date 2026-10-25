class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        self.maxHeap = stones
        heapq.heapify_max(self.maxHeap)

        while len(self.maxHeap) > 1:
            largest = heapq.heappop_max(self.maxHeap)
            second = heapq.heappop_max(self.maxHeap)
            if largest > second:
                heapq.heappush_max(self.maxHeap, largest - second)
        
        if len(self.maxHeap) == 0:
            return 0
        return self.maxHeap[0]
