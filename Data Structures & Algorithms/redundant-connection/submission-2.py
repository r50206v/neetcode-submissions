class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        visit = {}

        for u, v in edges:
            su = visit.get(u)
            sv = visit.get(v)

            if su is not None and su is sv:
                return [u, v]
            elif su is None and sv is None:
                new_set = set([u, v])
                visit[u] = new_set
                visit[v] = new_set
            elif su is None:
                visit[v].add(u)
                visit[u] = visit[v]
            elif sv is None:
                visit[u].add(v)
                visit[v] = visit[u]
            else:
                new_set = visit[u].union(visit[v])
                for x in new_set:
                    visit[x] = new_set
        return []