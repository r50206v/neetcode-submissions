class Solution:
    def partition(self, s: str) -> List[List[str]]:
        ans = []
        path = []

        def dfs(start):
            if start == len(s):
                ans.append(path[:])
                return 
            
            for end in range(start + 1, len(s) + 1):
                if s[start:end] == s[start:end][::-1]:
                    path.append(s[start:end])
                    dfs(end)
                    path.pop()
            
        dfs(0)
        return ans
