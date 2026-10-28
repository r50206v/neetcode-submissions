class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # from collections import Counter
        # freq = Counter(nums)

        # from operator import itemgetter
        # ans = sorted(list(freq.items()), key=itemgetter(1), reverse=True)
        # return [a[0] for a in ans[:k]]
        
        from collections import Counter
        freq = Counter(nums)
        max_n = max(freq.values())

        bucket = defaultdict(list)
        for key, val in freq.items():
            bucket[val].append(key)

        ans = []
        while k > 0:
            if bucket.get(max_n):
                ans.extend(bucket.get(max_n))
                k -= len(bucket.get(max_n))
            max_n -= 1
                
        return ans
