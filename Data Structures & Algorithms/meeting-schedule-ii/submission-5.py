"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        if intervals: 
            intervals.sort(key=lambda x: (x.start, x.end))
            ans = [intervals[0].end]
            heapq.heapify(ans)

            for intv in intervals[1:]:
                if ans[0] <= intv.start: 
                    heapq.heappop(ans)
                    heapq.heappush(ans, intv.end)
                elif ans[0] > intv.start: 
                    heapq.heappush(ans, intv.end)
            return len(ans)
        else: 
            return 0