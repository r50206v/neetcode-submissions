class Solution:
    def isPalindrome(self, s: str) -> bool:
        # import re
        # s_cleaned = re.sub(r'[^A-Za-z0-9]', '', s)
        # s_reverse_cleaned = s_cleaned[::-1]
        # return s_cleaned.lower() == s_reverse_cleaned.lower()

        i = 0
        j = len(s) - 1
        while i < j:
            if s[i].lower() == s[j].lower():
                i += 1
                j -= 1
            elif not (s[i].isdigit() or s[i].isalpha()):
                i += 1
            elif not (s[j].isdigit() or s[j].isalpha()):
                j -= 1
            else:
                return False
        return True

