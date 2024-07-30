class Solution(object):
    def isPalindrome(self, x):
        original=x
        reversed=0
        if x<0:
            return False
        else:
            while(x!=0):
                digit=x%10
                reversed=reversed*10+digit
                x//=10
        return original==reversed


        