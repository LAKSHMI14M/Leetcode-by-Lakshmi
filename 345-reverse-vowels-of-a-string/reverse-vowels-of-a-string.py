class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels="aeiouAEIOU"
        l=[]
        for i in s:
            if i in vowels:
                l.append(i)
        result=[]
        for i in s:
            if i in vowels:
                result.append(l.pop())
            else:
                result.append(i)
        return ''.join(result)


        