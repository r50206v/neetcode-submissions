class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        
        # Map each course to its prerequisites
        preMap = {i: [] for i in range(numCourses)}
        for crs, pre in prerequisites:
            preMap[crs].append(pre)
        visit = [0] * numCourses

        ans = []
        def dfs(crs):
            if visit[crs] == 1:
                return False # detect cycle
            if visit[crs] == 2:
                return True # end of the path

            visit[crs] = 1
            for pre in preMap[crs]:
                if not dfs(pre):
                    return False
            visit[crs] = 2
            ans.append(crs)
            return True
        
        for c in range(numCourses):
            if not dfs(c):
                return []
        return ans


