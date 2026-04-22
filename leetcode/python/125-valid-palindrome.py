class Solution:
    def isPalindrome(self, s: str) -> bool:
        formattedS = "".join([c for c in s.lower() if c.isalnum()])
        reversedS = "".join(reversed(formattedS))
        return formattedS == reversedS

    def isPalindromeTwoPointers(self, s: str) -> bool:
        formattedS = "".join([c for c in s.lower() if c.isalnum()])
        left = 0
        right = len(formattedS) - 1
        while left < right:
            if formattedS[left] != formattedS[right]:
                return False
            left += 1
            right -= 1
        return True
