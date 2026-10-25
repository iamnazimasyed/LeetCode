class Solution:
    def isPalindrome(self, s: str) -> bool:
        rev = ""
        result = ""

        for ch in s:
            if ch.isalnum():
                result += ch.lower()
                rev = ch.lower() + rev
        if rev == result:
            return True
        else:
            return False
                        