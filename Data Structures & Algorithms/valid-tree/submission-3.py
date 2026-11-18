class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        visit = {}

        for u, v in edges:
            su = visit.get(u)
            sv = visit.get(v)

            if su is not None and su is sv:
                return False
            elif su is None and sv is None: 
                new_set = set([u, v])
                visit[u] = new_set
                visit[v] = new_set
                n -= 1
            elif su is None:
                visit[v].add(u)
                visit[u] = visit[v]
                n -= 1
            elif sv is None: 
                visit[u].add(v)
                visit[v] = visit[u]
                n -= 1
            else: 
                if len(visit[u]) < len(visit[v]):
                    visit[v].update(visit[u])
                    smaller = visit[u]
                    bigger = visit[v]
                else: 
                    visit[u].update(visit[v])
                    smaller = visit[v]
                    bigger = visit[u]
                
                for node in smaller:
                    visit[node] = bigger
                n -= 1
        return n == 1