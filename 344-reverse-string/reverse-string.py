class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        n=len(s)
        i=0
        while i<n//2 :  
            s[i],s[n-i-1]=s[n-i-1],s[i]
            i+=1
        return s