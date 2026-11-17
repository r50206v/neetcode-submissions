class NumMatrix:

    def __init__(self, matrix: list[list[int]]):
        self.grid = matrix
        self.row_len = len(matrix)
        self.col_len = len(matrix[0])
        self.precompute_sum_grid = [[None for c in range(self.col_len)] for r in range(self.row_len)]
        self.dfs(self.row_len-1, self.col_len-1)
        
    def dfs(self, idx, jdx):
        if 0 <= idx < self.row_len and 0 <= jdx < self.col_len: 
            if self.precompute_sum_grid[idx][jdx] is not None:
                return self.precompute_sum_grid[idx][jdx]

            self.precompute_sum_grid[idx][jdx] = (
                self.dfs(idx-1, jdx)
                + self.dfs(idx, jdx-1)
                - self.dfs(idx-1, jdx-1) 
                + self.grid[idx][jdx]
            )
            return self.precompute_sum_grid[idx][jdx]
        else: 
            return 0

    def get_acc_sum(self, idx, jdx):
        if 0 <= idx < self.row_len and 0 <= jdx < self.col_len: 
            return self.precompute_sum_grid[idx][jdx]
        else:
            return 0

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        ans = (
            self.get_acc_sum(row2, col2)
            - self.get_acc_sum(row1-1, col2)
            - self.get_acc_sum(row2, col1-1)
            + self.get_acc_sum(row1-1, col1-1)
        )
        return ans


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)