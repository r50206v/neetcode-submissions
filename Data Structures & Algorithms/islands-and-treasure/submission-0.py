class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        row_len = len(grid)
        col_len = len(grid[0])

        q = deque()
        for r in range(row_len):
            for c in range(col_len):
                if grid[r][c] == 0:
                    q.append((r, c, 0))
        
        while q: 
            idx, jdx, dist = q.popleft()

            for i, j in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                if 0 <= idx+i < row_len and 0 <= jdx+j < col_len:
                    if grid[idx+i][jdx+j] == 2147483647:
                        grid[idx+i][jdx+j] = dist + 1
                        q.append((idx+i, jdx+j, dist+1))

