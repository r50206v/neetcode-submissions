class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        from collections import Counter
        countMap = Counter(tasks)
        freq = list(countMap.values())
        heapq.heapify_max(freq)

        time = 0
        queue = deque()
        while queue or freq: 
            time += 1
            
            if queue and queue[0][1] == time:
                remaining, _ = queue.popleft()
                heapq.heappush_max(freq, remaining)

            if freq:
                f = heapq.heappop_max(freq)
                if f > 1:
                    queue.append((f - 1, time + n + 1))
            else:
                continue
        
        return time