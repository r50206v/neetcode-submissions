class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans = []
        path = []
        def dfs(open, close):
            if len(path) == 2*n and open == close:
                ans.append("".join(path))
                return
            elif len(path) == 2*n:
                return

            if close > open:
                return
            
            path.append("(")
            if open < n:
                dfs(open + 1, close)
            path.pop()
            
            path.append(")")
            dfs(open, close + 1)
            path.pop()
        
        dfs(0, 0)
        return ans