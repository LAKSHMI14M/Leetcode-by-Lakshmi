class Solution:
    def longestPalindrome(self, s: str) -> str:
        n=len(s)
        longest=''
        for i in range(n):
            for j in range(i,n):
                substring=s[i:j+1]
                if self.ispalindrome(substring) and len(substring)>len(longest):
                    longest=substring
        return longest
    def ispalindrome(self, s: str) -> bool:
        return s==s[::-1]

        