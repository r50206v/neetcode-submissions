class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = deque([])
        ans = 0
        if len(tokens) == 1:
            return int(tokens[0])

        for c in tokens:
            if c.lstrip('-').isnumeric():
                stack.append(int(c))
            else:
                num2 = stack.pop()
                num1 = stack.pop()

                if c == '+':
                    ans = num1 + num2
                elif c == '-':
                    ans = num1 - num2
                elif c == '*': 
                    ans = num1 * num2
                elif c == '/':
                    ans = int(num1 / num2)

                stack.append(ans)
        return int(ans)
