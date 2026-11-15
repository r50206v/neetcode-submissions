class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        
        def dist_to_org(x, y):
            return math.sqrt(x**2 + y**2)

        distList = [(p[0], p[1], dist_to_org(p[0], p[1])) for p in points]
        ans = heapq.nsmallest(k, distList, key=lambda x: x[2])

        return [[a[0], a[1]] for a in ans]