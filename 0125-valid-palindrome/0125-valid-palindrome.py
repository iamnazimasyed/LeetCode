class Solution:
    def isPalindrome(self, s: str) -> bool:
        result = ""

        for ch in s:
            if ch.isalnum():
                result += ch.lower()
            rev = result[::-1]
        if rev == result:
            return True
        else:
            return False
                