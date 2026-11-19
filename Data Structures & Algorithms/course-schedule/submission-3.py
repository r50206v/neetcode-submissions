class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        safe = set([])
        node = {i: [] for i in range(numCourses)}
        for p in prerequisites:
            node[p[0]].append(p)

        def dfs(n, path):
            if n in safe:
                return True
            if n in path: 
                return False
            
            path.add(n)
            ans = True
            for pre in node[n]:
                ans = ans and dfs(pre[1], path)
            path.remove(n)
            return ans

        for c in prerequisites:
            if not dfs(c[0], set([])): 
                return False
            else: 
                safe.add(c[0])
        return True
