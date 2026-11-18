class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        visit = {}

        for u, v in edges: 
            su = visit.get(u)
            sv = visit.get(v)

            if su is not None and su is sv: 
                pass

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
                if len(visit[v]) < len(visit[u]):
                    visit[u].update(visit[v])
                    bigger = visit[u]
                    smaller = visit[v]
                else: 
                    visit[v].update(visit[u])
                    bigger = visit[v]
                    smaller = visit[u]
                
                for node in smaller:
                    visit[node] = bigger
                n -= 1
        
        return n
