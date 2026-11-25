class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas) >= sum(cost):
            total = 0
            res = 0
            for idx in range(len(gas)): 
                if total + gas[idx] - cost[idx] < 0:
                    total = 0
                    res = idx + 1
                else: 
                    total += gas[idx] - cost[idx]
            return res
        return -1
