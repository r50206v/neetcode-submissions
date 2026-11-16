class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ans = 0
        rowN = len(grid)
        colN = len(grid[0])

        def dfs(idx, jdx): 
            if 0 <= idx < rowN and 0 <= jdx < colN:
                if grid[idx][jdx] == 0:
                    return 0
            
                grid[idx][jdx] = 0

                return (
                    1
                    + dfs(idx + 1, jdx)
                    + dfs(idx - 1, jdx)
                    + dfs(idx, jdx + 1)
                    + dfs(idx, jdx - 1)
                )

            else: 
                return 0
        
        for r in range(rowN):
            for c in range(colN):
                if grid[r][c] == 1:
                    ans = max(ans, dfs(r, c))
        return ans