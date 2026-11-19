class Solution:
    def solve(self, board: List[List[str]]) -> None:
        ROWS = len(board)
        COLS = len(board[0])
        
        # def dfs(idx, jdx, path):
        #     if (idx == 0 or idx == ROWS-1 or jdx == 0 or jdx == COLS-1) and board[idx][jdx] == 'O':
        #         return True, set([])
        #     elif (idx == 0 or idx == ROWS-1 or jdx == 0 or jdx == COLS-1) and board[idx][jdx] == 'X': 
        #         return False, path
            
        #     touch_wall = False
        #     if (idx, jdx) not in path and board[idx][jdx] == 'O':
        #         path.add((idx, jdx))
        #         for i, j in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
        #             if 0 <= idx + i < ROWS and 0 <= jdx + j < COLS and board[idx+i][jdx+j] == 'O':
        #                 touch_wall, path = dfs(idx+i, jdx+j, path)
        #                 if touch_wall:
        #                     return True, set([])
        #     return False, path

        def is_edge(idx, jdx):
            return (idx == 0) or (idx == ROWS - 1) or (jdx == 0) or (jdx == COLS - 1)

        def bfs(idx, jdx):
            if is_edge(idx, jdx) and board[idx][jdx] == 'O': 
                return set([])

            q = deque([(idx, jdx)])
            path = set([(idx, jdx)])
            while q: 
                idx, jdx = q.popleft()
                for i, j in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                    is_edge_bool = is_edge(idx + i, jdx + j)
                    if not is_edge_bool and board[idx+i][jdx+j] == 'O' and (idx+i, jdx+j) not in path:
                        q.append((idx+i, jdx+j))
                        path.add((idx+i, jdx+j))
                        visited.add((idx+i, jdx+j))
                    elif is_edge_bool and board[idx+i][jdx+j] == 'O' and (idx+i, jdx+j) not in path:
                        visited.add((idx+i, jdx+j))
                        return set([])
            return path

        visited = set([])
        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == 'O' and (r, c) not in visited:
                    p = bfs(r, c)
                    visited.update(p)
                    for i, j in p:
                        board[i][j] = 'X'
        return None



