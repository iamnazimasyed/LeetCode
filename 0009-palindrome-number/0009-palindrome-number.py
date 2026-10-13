class Solution:
    def isPalindrome(self, x: int) -> bool:
        original = x
        rev=0
        n = abs(x)
        while n > 0:
            digit = n%10
            rev=rev*10+digit
            n=n//10
        if rev == original:
            return True
        else:
            return False
      

        