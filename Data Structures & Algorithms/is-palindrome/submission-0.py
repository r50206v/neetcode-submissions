class Solution:
    def isPalindrome(self, s: str) -> bool:
        import re
        s_cleaned = re.sub(r'[^A-Za-z0-9]', '', s)
        s_reverse_cleaned = s_cleaned[::-1]
        return s_cleaned.lower() == s_reverse_cleaned.lower()