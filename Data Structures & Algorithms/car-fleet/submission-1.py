class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        import itertools
        from operator import itemgetter
        sorted_array = sorted(zip(position, speed), key=itemgetter(0), reverse=True)

        stack = []
        for p, s in sorted_array:
            arr = (target - p) / s

            if len(stack) == 0:
                stack.append(arr)
            
            elif stack and stack[-1] >= arr:
                continue
            
            elif stack and stack[-1] < arr:
                stack.append(arr)
        
        return len(stack)