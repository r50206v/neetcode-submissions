class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row = defaultdict(set)
        col = defaultdict(set)
        squ = defaultdict(set)

        for jdx in range(len(board)):
            for idx in range(len(board[0])):
                if board[idx][jdx] == '.':
                    continue

                val = board[idx][jdx]
                # validating row
                if val not in row[idx]:
                    row[idx].add(val)
                else: 
                    print(idx, jdx, val, 'row', row[idx])
                    return False

                # validating col
                if val not in col[jdx]:
                    col[jdx].add(val)
                else: 
                    print(idx, jdx, val, 'col', col[jdx])
                    return False

                # validating squ
                squ_idx = (jdx // 3) * 3 + idx // 3
                if val not in squ[squ_idx]:
                    squ[squ_idx].add(val)
                else: 
                    print(idx, jdx, val, 'squ', squ[squ_idx])
                    return False
        return True
        
