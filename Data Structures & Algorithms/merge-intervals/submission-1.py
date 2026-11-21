# class Solution:
#     def merge(self, intervals: List[List[int]]) -> List[List[int]]:
#         int_sorted = sorted(intervals, key=lambda x: (x[0], x[1]))
#         print(int_sorted)

#         idx = 1
#         while idx < len(int_sorted):
#             # print(idx, int_sorted[idx-1], int_sorted[idx])
#             if int_sorted[idx-1][1] >= int_sorted[idx][0]:
#                 int_sorted[idx-1] = [
#                     int_sorted[idx-1][0],
#                     int_sorted[idx][1]
#                 ]
#             else: 
#                 idx += 1
#         return int_sorted
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x: (x[0], x[1]))
        ans = [intervals[0]]
        for intv in intervals[1:]: 
            if ans[-1][1] >= intv[0]:
                ans[-1] = [
                    ans[-1][0], 
                    max(intv[1], ans[-1][1])
                ]
            else: 
                ans.append(intv)
        return ans