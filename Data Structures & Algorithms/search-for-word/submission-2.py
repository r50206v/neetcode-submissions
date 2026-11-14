class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rowN = len(board)
        colN = len(board[0])
        visited = [[0 for _ in range(colN)] for _ in range(rowN)]

        def dfs(w, idx, jdx):
            if w == "":
                return True
            if idx < 0 or idx == rowN or jdx < 0 or jdx == colN:
                return False
            if visited[idx][jdx] == 1 or board[idx][jdx] != w[0]:
                return False
            
            visited[idx][jdx] = 1
            found = (
                dfs(w[1:], idx + 1, jdx) 
                or dfs(w[1:], idx - 1, jdx) 
                or dfs(w[1:], idx, jdx + 1) 
                or dfs(w[1:], idx, jdx - 1)
            )
            visited[idx][jdx] = 0
            return found
        
        for i in range(len(board)):
            for j in range(len(board[0])):
                if dfs(word, i, j):
                    return True
        return False
        