# class Solution:
#     def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
#         intervals.sort(key=lambda x: x[0])
#         prev_end = intervals[0][1]
#         rm_count = 0

#         for start, end in intervals[1:]:
#             if prev_end > start:
#                 prev_end = min(prev_end, end)
#                 rm_count += 1
#             else:
#                 prev_end = end
#         return rm_count
class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        if not intervals:
            return 0

        intervals.sort(key=lambda x: x[0])
        prev_end = intervals[0][1]
        rm_count = 0

        for intv in intervals[1:]:
            if prev_end > intv[0]:
                prev_end = min(intv[1], prev_end)
                rm_count += 1
            else:
                prev_end = intv[1]
        return rm_count

