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
            for pre in node[n]:
                check = dfs(pre[1], path)
                if check:
                    safe.add(pre[1])
                else: 
                    return False
            path.remove(n)
            return True

        for c in prerequisites:
            if not dfs(c[0], set([])): 
                return False
        return True
