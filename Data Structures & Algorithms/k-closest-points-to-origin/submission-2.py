class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        
        def dist_to_org(x, y):
            return math.sqrt(x**2 + y**2)

        ans = heapq.nsmallest(
            k, points, key=lambda x: dist_to_org(x[0], x[1])
        )

        return ans