class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        senate = list(senate)
        senate_len = len(senate)
        r_queue = deque()
        d_queue = deque()

        for idx, val in enumerate(senate): 
            if val == 'R':
                r_queue.append(idx)
            else:
                d_queue.append(idx)

        while r_queue and d_queue:
            r_idx = r_queue.popleft()
            d_idx = d_queue.popleft()
            
            if r_idx < d_idx:
                r_queue.append(r_idx + senate_len)
            else: 
                d_queue.append(d_idx + senate_len)
        
        if r_queue:
            return "Radiant"
        elif d_queue:
            return "Dire"