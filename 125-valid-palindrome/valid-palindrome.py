class Solution(object):
    def isPalindrome(self, s):
        A=s.lower()
        original=''.join(char for char in A if char.isalnum())
        reversed=original[::-1]
        return reversed==original
        