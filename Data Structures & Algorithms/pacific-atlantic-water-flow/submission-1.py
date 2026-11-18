# class Solution:
#     def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
#         row_len = len(heights)
#         col_len = len(heights[0])

#         def check_pacific(i, j, visit):
#             if i == 0 or j == 0: 
#                 return True 
            
#             ans = False
#             for n_i, n_j in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
#                 if 0 <= i+n_i < row_len and 0 <= j+n_j < col_len:
#                     if (i+n_i, j+n_j) not in visit and heights[i][j] >= heights[i+n_i][j+n_j]:
#                         visit.append((i+n_i, j+n_j))
#                         ans = ans or check_pacific(i+n_i, j+n_j, visit) 
#             return ans
        
#         def check_atlantic(i, j, visit):
#             if i == row_len - 1 or j == col_len - 1: 
#                 return True 
            
#             ans = False
#             for n_i, n_j in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
#                 if 0 <= i+n_i < row_len and 0 <= j+n_j < col_len:
#                     if (i+n_i, j+n_j) not in visit and heights[i][j] >= heights[i+n_i][j+n_j]:
#                         visit.append((i+n_i, j+n_j))
#                         ans = ans or check_atlantic(i+n_i, j+n_j, visit) 
#             return ans

#         res = []
#         for idx in range(row_len):
#             for jdx in range(col_len):
#                 if check_pacific(idx, jdx, [(idx, jdx)]) and check_atlantic(idx, jdx, [(idx, jdx)]):
#                     res.append([idx, jdx])
#         return res


class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ROWS, COLS = len(heights), len(heights[0])
        pac, atl = set(), set()

        def dfs(r, c, visit, prevHeight):
            if ((r, c) in visit or
                r < 0 or c < 0 or
                r == ROWS or c == COLS or
                heights[r][c] < prevHeight
            ):
                return
            visit.add((r, c))
            dfs(r + 1, c, visit, heights[r][c])
            dfs(r - 1, c, visit, heights[r][c])
            dfs(r, c + 1, visit, heights[r][c])
            dfs(r, c - 1, visit, heights[r][c])

        for c in range(COLS):
            dfs(0, c, pac, heights[0][c])
            dfs(ROWS - 1, c, atl, heights[ROWS - 1][c])

        for r in range(ROWS):
            dfs(r, 0, pac, heights[r][0])
            dfs(r, COLS - 1, atl, heights[r][COLS - 1])

        res = []
        for r in range(ROWS):
            for c in range(COLS):
                if (r, c) in pac and (r, c) in atl:
                    res.append([r, c])
        return res