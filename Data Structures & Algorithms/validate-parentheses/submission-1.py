class Solution:
    def isValid(self, s: str) -> bool:
        mapping = {
            '[': ']',
            '{': '}',
            '(': ')',
        }

        stack = []
        for val in list(s):
            if val in mapping.keys():
                stack.append(mapping[val])
            elif len(stack) > 0 and stack[-1] == val:
                stack.pop()
                continue
            else:
                return False

        return len(stack) == 0
                