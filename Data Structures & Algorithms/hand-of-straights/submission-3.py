from collections import Counter
class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if groupSize == 1: 
            return True
        if len(hand) % groupSize != 0:
            return False 

        countMap = Counter(hand)
        hand.sort()

        for smallest in hand: 
            if countMap.get(smallest, 0) > 0:
                for i in range(0, groupSize, 1):
                    if countMap.get(smallest + i, 0) > 0:
                        countMap[smallest + i] -= 1
                    else:
                        return False
        return True


            
            