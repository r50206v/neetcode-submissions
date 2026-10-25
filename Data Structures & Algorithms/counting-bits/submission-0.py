class Solution:
    def countBits(self, n: int) -> List[int]:
        dp = [0] * (n + 1)
        offset = 1

        for idx in range(1, len(dp)):
            if offset * 2 == idx:
                offset = idx
            
            dp[idx] = 1 + dp[idx - offset]
            
        return dp