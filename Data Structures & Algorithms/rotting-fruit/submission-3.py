class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        row_len = len(grid)
        col_len = len(grid[0])

        q = deque()
        for r in range(row_len):
            for c in range(col_len):
                if grid[r][c] == 2:
                    q.append((r, c, 0))
        
        ans = 0
        while q: 
            idx, jdx, t = q.popleft()
            ans = max(ans, t)

            for i, j in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                if 0 <= idx + i < row_len and 0 <= jdx + j < col_len:
                    if grid[idx + i][jdx + j] == 1:
                        q.append((idx + i, jdx + j, t + 1))
                        grid[idx + i][jdx + j] = 2
        
        rem = sum([sum([c == 1 for c in r]) for r in grid])
        if rem > 0:
            return -1
        return ans

