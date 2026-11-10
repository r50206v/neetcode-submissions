class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []
        path = []
        candidates.sort()

        def dfs(idx, remain):
            if remain == 0:
                ans.append(path[:])
                return
            elif idx == len(candidates) or remain < 0: 
                return 

            path.append(candidates[idx])
            dfs(idx + 1, remain - candidates[idx])

            path.pop()
            nxt = idx + 1
            while nxt < len(candidates) and candidates[nxt] == candidates[idx]:
                nxt += 1
            dfs(nxt, remain)
        
        dfs(0, target)
        return ans 

