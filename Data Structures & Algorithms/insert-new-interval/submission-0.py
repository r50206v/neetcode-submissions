class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        intervals.sort(key=lambda x: (x[0], x[1]))

        import bisect
        bisect.insort(intervals, newInterval)
        # pos = bisect.bisect(intervals, newInterval)

        # intervals.insert(pos, newInterval)
        # pop_pos = False
        # if intervals[pos-1][1] >= intervals[pos]:
        #     intervals[pos-1] = [
        #         intervals[pos-1][0], 
        #         max(intervals[pos-1][1], intervals[pos][1])
        #     ]
        #     pop_pos = True
        # if intervals[pos-1][1] >= intervals[pos]:
        #     intervals[pos-1] = [
        #         intervals[pos-1][0], 
        #         max(intervals[pos-1][1], intervals[pos][1])
        #     ]

        ans = [intervals[0]]
        for intv in intervals[1:]:
            if ans[-1][1] >= intv[0]:
                ans[-1] = [
                    ans[-1][0], 
                    max(ans[-1][1], intv[1])
                ]
            else: 
                ans.append(intv)
        return ans


