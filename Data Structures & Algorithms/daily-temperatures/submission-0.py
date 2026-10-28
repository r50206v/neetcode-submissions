class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        ans = [0] * len(temperatures)

        # for idx, temp in enumerate(temperatures):
        #     while stack and temp > stack[-1][1]:
        #         lst_idx, lst_temp = stack.pop()
        #         ans[lst_idx] = idx - lst_idx
        #     stack.append((idx, temp))
        
        # return ans

        for idx in range(len(temperatures)):
            if len(stack) == 0:
                stack.append((idx, temperatures[idx]))

            elif stack[-1][1] < temperatures[idx]:
                while stack and stack[-1][1] < temperatures[idx]:
                    lst_idx, lst_temp = stack.pop()
                    ans[lst_idx] = idx - lst_idx
                
            stack.append((idx, temperatures[idx]))
        
        return ans