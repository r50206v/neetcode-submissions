"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        intervals.sort(key=lambda x: x.start)
        ans = []
        # heapq.heapify(ans) # unnecessary because theres only one item

        for intv in intervals:
            if ans and ans[0] <= intv.start: 
                heapq.heappop(ans)
                heapq.heappush(ans, intv.end)
            else: # ans[0] > intv.start
                heapq.heappush(ans, intv.end)
        return len(ans)